"""Sample blind human-vs-model Python solutions from serafeimdossas/ai-code-detection (MIT).

Only CodeNet tasks are used; the Rosetta Code half of that dataset carries GFDL text.
Each task gets four solutions (one human, three models) under neutral names a.py..d.py
in a seeded random order. manifest.json holds who wrote which; do not show it to the skill.

Usage: python evals/scripts/import_codenet_pairs.py <path/to/ai_code_detection.parquet> [n_tasks]
Needs pyarrow. Parquet: https://huggingface.co/datasets/serafeimdossas/ai-code-detection
"""

import json
import random
import sys
from collections import defaultdict
from pathlib import Path

import pyarrow.parquet as pq

OUT = Path(__file__).resolve().parent.parent / "external" / "codenet-blind"
GENERATORS = ["Human", "OpenAI o4-mini", "Gemini 2.5 Flash-Lite", "Claude 3.5 Haiku"]
MAX_LINES = 120


def main() -> None:
    rows = pq.read_table(sys.argv[1]).to_pylist()
    n_tasks = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    rng = random.Random(20260929)

    by_task: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        if row["source"] == "CodeNet":
            by_task[row["task_name"]][row["generator"]].append(row)

    def usable(solutions: list[dict]) -> list[dict]:
        return [s for s in solutions if 5 <= len(s["code"].splitlines()) <= MAX_LINES]

    candidates = sorted(
        task for task, gens in by_task.items() if all(usable(gens[g]) for g in GENERATORS)
    )
    # Prefer tasks where the model answers are long enough to carry some structure.
    candidates.sort(key=lambda t: -sum(len(usable(by_task[t][g])[0]["code"].splitlines()) for g in GENERATORS[1:]))
    chosen = sorted(candidates[: n_tasks * 2])
    chosen = rng.sample(chosen, n_tasks)

    manifest = []
    for i, task in enumerate(sorted(chosen), 1):
        picks = [(g, rng.choice(usable(by_task[task][g]))) for g in GENERATORS]
        rng.shuffle(picks)
        folder = OUT / f"task-{i:02d}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "TASK.md").write_text(f"# {task}\n\n{picks[0][1]['task_description'].strip()}\n")
        entry = {"folder": str(folder.relative_to(OUT.parent.parent)), "task": task, "files": {}}
        for letter, (generator, row) in zip("abcd", picks):
            (folder / f"{letter}.py").write_text(row["code"].replace("\xa0", " ").rstrip() + "\n")
            entry["files"][f"{letter}.py"] = generator
        manifest.append(entry)

    (OUT / "manifest.json").write_text(json.dumps({
        "source": "https://huggingface.co/datasets/serafeimdossas/ai-code-detection",
        "license": "MIT (dataset); human solutions come from IBM Project CodeNet",
        "note": "Blind set. Never pass this file to the skill under test.",
        "tasks": manifest,
    }, indent=2) + "\n")
    print(f"{len(manifest)} tasks -> {OUT}")


if __name__ == "__main__":
    main()
