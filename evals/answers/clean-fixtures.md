# Expected findings: clean fixtures (false-positive checks)

All of these should score 0 to 1 with no high or med findings.

## clean-ts/retry.ts
- try/catch has real recovery (retry with backoff) and keeps `cause`. `parseLimit` validates untrusted query input.

## clean-ts-webhook/webhook.ts
- Env check at startup (boundary), signature check (security), JSON parse with 400 (boundary), comments explain why. `SECRET!` after a module-level throw is acceptable (TS cannot narrow across the function boundary).

## clean-py-cli/dedupe.py
- `print` is the program's output (CLI), not debug residue. The local `import json` has a reason comment. `is_dir` check validates CLI input. Exit codes are deliberate.
