"""Import TS and Python fixtures from mgiovani/stopslop (MIT) as blind eval cases.

The upstream fixtures carry their answers inline (`// expect: SLOP005`, trailing
`# expect-line: 6 SLOP042`). The skill would read those, so this script strips
them and writes the answers to labels.json instead, mapped to our pattern IDs.

Usage: python3 evals/scripts/import_stopslop.py [commit-sha]
Needs the `gh` CLI (for the tree listing) and network access.
"""

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = "mgiovani/stopslop"
OUT = Path(__file__).resolve().parent.parent / "external" / "stopslop"
LANGS = {"typescript", "python"}

# stopslop rule -> (upstream name, our pattern id from skills/deslop/references/patterns.md)
RULES = {
    "SLOP001": ("elision / 'rest unchanged' comment", "R7"),
    "SLOP002": ("chat preamble leaked into code", "C3"),
    "SLOP003": ("stray markdown code fence", "R7"),
    "SLOP004": ("AI attribution / chat-share artifact", "C3"),
    "SLOP005": ("empty or log-only catch", "D1"),
    "SLOP006": ("broad or swallowing except", "D1"),
    "SLOP007": ("type escape (as any, as unknown as T, @ts-ignore)", "T1"),
    "SLOP008": ("stub-only / unimplemented body", "R3"),
    "SLOP009": ("placeholder or sample credential value", "R3"),
    "SLOP037": ("reinvented stdlib / platform feature", "V5"),
    "SLOP038": ("dependency with a stdlib equivalent", "V5"),
    "SLOP039": ("pass-through wrapper function", "O1"),
    "SLOP040": ("single-implementation interface / abstract class", "O2"),
    "SLOP042": ("comment that restates the code", "C1"),
    "SLOP043": ("comment that runs long", "C1"),
    "SLOP045": ("mechanical formatting uniformity", "R6"),
}

# Either its own comment (`code  // expect: X`) or appended to one (`// @ts-ignore expect: X`).
INLINE = re.compile(r"(?:\s*(?://|#)\s*|\s+)expect:\s*(SLOP[A-Z0-9, ]*?)\s*$")
TRAILING = re.compile(r"^\s*(//|#)\s*expect-line:\s*(\d+)\s+([A-Z0-9, ]+?)\s*$")


def sh(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def rules(text: str) -> list[str]:
    return [r.strip() for r in text.split(",") if r.strip()]


def strip(source: str) -> tuple[str, list[tuple[int, str]]]:
    lines = source.splitlines()
    labels: list[tuple[int, str]] = []
    kept: list[str] = []
    for n, line in enumerate(lines, 1):
        trailing = TRAILING.match(line)
        if trailing:
            labels += [(int(trailing.group(2)), r) for r in rules(trailing.group(3))]
            continue
        inline = INLINE.search(line)
        if inline:
            labels += [(n, r) for r in rules(inline.group(1))]
            line = line[: inline.start()]
        kept.append(line)
    # Trailing marker lines sit after all code, so line numbers above them are unchanged.
    while kept and not kept[-1].strip():
        kept.pop()
    return "\n".join(kept) + "\n", sorted(labels)


def main() -> None:
    sha = sys.argv[1] if len(sys.argv) > 1 else sh("gh", "api", f"repos/{REPO}/commits/HEAD", "--jq", ".sha").strip()
    paths = sh("gh", "api", f"repos/{REPO}/git/trees/{sha}?recursive=1", "--jq", '.tree[] | select(.type=="blob") | .path').split()
    OUT.mkdir(parents=True, exist_ok=True)
    cases = []
    for path in paths:
        parts = path.split("/")
        if len(parts) != 4 or parts[:2] != ["tests", "fixtures"] or parts[2] not in LANGS:
            continue
        name = parts[3]
        if not name.startswith(("slop_", "clean_")) or name.endswith(".pyi"):
            continue
        raw = urllib.request.urlopen(f"https://raw.githubusercontent.com/{REPO}/{sha}/{path}").read().decode()
        text, labels = strip(raw)
        dest = OUT / parts[2] / name
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(text)
        cases.append({
            "file": str(dest.relative_to(OUT.parent.parent)),
            "kind": "slop" if name.startswith("slop_") else "clean",
            "expected": [
                {"line": line, "upstream_rule": r, "upstream_name": RULES.get(r, ("?", None))[0], "pattern": RULES.get(r, ("?", None))[1]}
                for line, r in labels
            ],
        })
    license_text = urllib.request.urlopen(f"https://raw.githubusercontent.com/{REPO}/{sha}/LICENSE").read().decode()
    (OUT / "LICENSE").write_text(license_text)
    (OUT / "labels.json").write_text(json.dumps({"source": f"https://github.com/{REPO}", "commit": sha, "license": "MIT", "cases": cases}, indent=2) + "\n")
    print(f"{len(cases)} cases, {sum(len(c['expected']) for c in cases)} labels -> {OUT}")


if __name__ == "__main__":
    main()
