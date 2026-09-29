"""Score deslop findings against a labeled set (stopslop labels.json format).

The skill writes findings as
    <n>. [<pattern id>] <file>:<line or range> | <severity> | ...
Save the skill's Step 2 output for a batch of files to a text file, then run:

    python3 evals/deslop/scripts/score_findings.py <output.txt> [labels.json] [--tolerance 2]

A label counts as found when a finding names the same file (by basename), a line
within the tolerance, and the same pattern family (first letter: C, D, O, V, T, S, R).
Clean files count as false positives when they get any high or med finding.
Files the output never mentions are listed separately, so a partial run is visible.
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

FINDING = re.compile(
    r"\[(?P<id>[A-Z]\d+)\]\s+`?(?P<file>[\w./-]+?\.(?:tsx?|jsx?|py))`?:(?P<start>\d+)(?:-(?P<end>\d+))?\s*\|\s*(?P<sev>high|med|low)",
    re.IGNORECASE,
)
DEFAULT_LABELS = Path(__file__).resolve().parent.parent / "external" / "stopslop" / "labels.json"


def parse(output: str) -> dict[str, list[dict]]:
    found = defaultdict(list)
    for m in FINDING.finditer(output):
        start = int(m["start"])
        found[Path(m["file"]).name].append({
            "id": m["id"].upper(),
            "start": start,
            "end": int(m["end"] or start),
            "sev": m["sev"].lower(),
        })
    return found


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("labels", nargs="?", default=str(DEFAULT_LABELS))
    ap.add_argument("--tolerance", type=int, default=2)
    args = ap.parse_args()

    output = Path(args.output).read_text()
    labels = json.loads(Path(args.labels).read_text())
    found = parse(output)
    mentioned = {Path(c["file"]).name for c in labels["cases"] if Path(c["file"]).name in output}

    hits = misses = false_pos = clean_ok = 0
    missed, noisy = [], []
    for case in labels["cases"]:
        name = Path(case["file"]).name
        if name not in mentioned:
            continue
        findings = found.get(name, [])
        if case["kind"] == "clean":
            loud = [f for f in findings if f["sev"] in ("high", "med")]
            if loud:
                false_pos += 1
                noisy.append(f"{name}: " + ", ".join(f"{f['id']}@{f['start']}" for f in loud))
            else:
                clean_ok += 1
            continue
        for exp in case["expected"]:
            family = (exp["pattern"] or "?")[0]
            ok = any(
                f["id"][0] == family
                and f["start"] - args.tolerance <= exp["line"] <= f["end"] + args.tolerance
                for f in findings
            )
            if ok:
                hits += 1
            else:
                misses += 1
                missed.append(f"{name}:{exp['line']} {exp['pattern']} ({exp['upstream_name']})")

    unseen = sorted(Path(c["file"]).name for c in labels["cases"] if Path(c["file"]).name not in mentioned)
    total = hits + misses
    print(f"recall: {hits}/{total} = {hits / total:.0%}" if total else "recall: no labeled slop files in output")
    clean_total = clean_ok + false_pos
    print(f"clean files without high/med findings: {clean_ok}/{clean_total}" if clean_total else "clean files: none in output")
    for line in missed:
        print("  missed", line)
    for line in noisy:
        print("  false positive", line)
    if unseen:
        print(f"not in output ({len(unseen)}): {', '.join(unseen[:10])}{' ...' if len(unseen) > 10 else ''}")


if __name__ == "__main__":
    main()
