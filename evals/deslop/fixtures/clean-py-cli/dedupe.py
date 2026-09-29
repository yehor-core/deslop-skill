#!/usr/bin/env python3
"""Find duplicate files under a directory by content hash."""

import argparse
import hashlib
import sys
from collections import defaultdict
from pathlib import Path


def file_hash(path: Path) -> str:
    h = hashlib.blake2b()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(root: Path) -> list[list[Path]]:
    by_size = defaultdict(list)
    for p in root.rglob("*"):
        if p.is_file() and not p.is_symlink():
            by_size[p.stat().st_size].append(p)

    # Hashing is the slow part; only files that share a size can be duplicates.
    by_hash = defaultdict(list)
    for same_size in by_size.values():
        if len(same_size) > 1:
            for p in same_size:
                by_hash[file_hash(p)].append(p)
    return [paths for paths in by_hash.values() if len(paths) > 1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args()

    if not args.root.is_dir():
        print(f"not a directory: {args.root}", file=sys.stderr)
        return 2

    groups = find_duplicates(args.root)
    if args.json:
        import json  # only needed for this flag

        print(json.dumps([[str(p) for p in g] for g in groups], indent=2))
    else:
        for group in groups:
            print("\n".join(str(p) for p in group), end="\n\n")
    return 0 if not groups else 1


if __name__ == "__main__":
    sys.exit(main())
