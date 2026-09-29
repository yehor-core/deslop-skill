# deslop evals

Test material for the `deslop` skill. Nothing here is loaded by the skill at runtime.

## Layout

```
evals.json            15 test prompts with expected behavior (skill-creator format)
fixtures/             hand-written cases, one folder per scenario
answers/              answer keys for fixtures; never give these to the skill under test
external/
  stopslop/           88 TS/Python files (44 slop, 44 clean) + labels.json, from mgiovani/stopslop (MIT)
  anti-slop/          115 TS snippets from dmmulroy/anti-slop rule tests (MIT), opinionated
  codenet-blind/      20 tasks x 4 solutions (1 human, 3 models) under neutral names, manifest.json is the key
scripts/
  import_stopslop.py      re-download stopslop fixtures, strip inline answers into labels.json
  import_anti_slop.mjs    re-extract anti-slop valid/invalid snippets
  import_codenet_pairs.py re-sample the blind CodeNet set (needs the parquet file and pyarrow)
  score_findings.py       score saved skill output against labels.json
```

## Fixtures

| Folder | What it tests |
| --- | --- |
| `ts-user-service` | Classic single-file slop: docstrings, try/catch into null, one-impl interface, compat alias |
| `ts-express-orders` | Validation repeated across route/service/repo, widen-then-assert, retry around in-memory work, hidden missing `await` |
| `ts-react-profile` | Chat artifacts ("Certainly! Here's...", "rest unchanged"), placeholder API key, hook and memo overkill, `moment` |
| `ts-duplicate-helpers` | Project-level duplicates that are not quite identical (UTC vs local time) |
| `py-config-loader` | Silent fallback to a default database, ABC + factory with one impl, weak tests |
| `py-fastapi-invoices` | Re-validating pydantic, dead bool flags, hallucinated import, fake-success catch-all |
| `py-tests-slop` | Test slop vs. weakened tests (bugs) and keeping coverage while deleting |
| `pr-drive-by` | Diff review: unrequested cache, swallowed error, drive-by reformat in a typo PR |
| `clean-ts`, `clean-ts-webhook`, `clean-py-cli` | False positives: boundary validation, real recovery, CLI prints |

## Rules for running

- Give the skill only the paths in each eval's `files`. `answers/`, `labels.json`, `snippets.json` `kind` fields, and `codenet-blind/manifest.json` are answer keys.
- The upstream stopslop files had `// expect: SLOP0xx` markers in the code; the import script removes them. Re-run it rather than copying files by hand.
- The skill is interactive. In `claude -p` runs, tell it how to answer the menu (for example "treat 'show the slop?' as yes, stop after Step 2").

## Scoring the labeled set

```bash
claude -p --plugin-dir . "Use the deslop skill. Find AI slop in every file in evals/external/stopslop/typescript. Treat 'show the slop?' as yes and stop after Step 2." > /tmp/ts-run.txt
python3 evals/scripts/score_findings.py /tmp/ts-run.txt
```

The scorer matches findings by file, line (plus or minus 2), and pattern family, and counts any high or med finding on a `clean_*` file as a false positive. stopslop and deslop disagree in a few places (stopslop calls `catch { return null }` clean; deslop may call it D1), so read the misses before tuning the skill.

## Sources

- stopslop fixtures: https://github.com/mgiovani/stopslop (MIT, see `external/stopslop/LICENSE`)
- anti-slop rule tests: https://github.com/dmmulroy/anti-slop (MIT, see `external/anti-slop/LICENSE`)
- CodeNet blind set: https://huggingface.co/datasets/serafeimdossas/ai-code-detection (MIT), built on IBM Project CodeNet
- Pattern ideas for hand-written fixtures: [22 patterns of AI code slop](https://dev.to/kirankunapuli/the-22-patterns-of-ai-code-slop-and-how-to-delete-13de), [20 AI slop code examples](https://scanaislop.com/blog/ai-slop-code-examples/), [How to de-slop an AI-generated codebase](https://www.builder.io/blog/de-slop-ai-generated-codebase)
