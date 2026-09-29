# Cleanup procedure

Read this at Step 4, after the user confirmed the plan. The goal: remove exactly the findings the user picked, keep behavior the same, and leave the work where the user can review it or throw it away.

## 1. Isolate the work

Check `git status --porcelain` and where the target files are.

- **Clean working tree**: create a branch in place, `git switch -c deslop/<short-slug>`. Dependencies (`node_modules`, `.venv`) keep working, so checks can run.
- **Uncommitted changes in unrelated files**: use a worktree so the user's work is not touched. Prefer the EnterWorktree tool if it is available; otherwise `git worktree add ../<repo>-deslop -b deslop/<short-slug>`. A new worktree has no `node_modules` or virtualenv. Point it at the existing ones (symlink `node_modules`, reuse the venv's interpreter). Installing dependencies runs package install scripts, so do it only if the user agreed to it in the plan, and say which you did.
- **Uncommitted changes in the target files**: a worktree would not contain them. Ask (see "Asking the user" in SKILL.md): "Commit my changes first, then clean on a branch" (recommended) or "Clean in place without a branch". Never stash or commit the user's work without that answer.
- **Not a git repository**: ask before editing. Offer "Edit in place" or "Show the cleaned code only".

The branch name goes in the report so the user can diff or delete it.

## 2. Record the baseline

Find the project's checks, in this order of trust: scripts in `package.json` (`test`, `typecheck`, `lint`), `Makefile` or `justfile` targets, CI config (`.github/workflows/*.yml`), then tool configs (`tsconfig.json` means `npx tsc --noEmit`; `pyproject.toml` with `[tool.pytest]`, `[tool.ruff]`, `[tool.mypy]`, `[tool.pyright]`).

Run only the commands listed in the plan the user approved at Step 3, exactly as listed. If you discover while working that another command is needed, ask first. Run them before editing and keep the results: which pass, which fail, and the failing test names. Failures that exist before the cleanup are not yours to fix; report them as pre-existing. If a full test suite takes more than a few minutes, run the tests that cover the target files and say so.

If the project has no checks at all, or the user chose not to run them, say so in the plan at Step 3, and be more careful: after cleanup at least import or compile each touched file (`node --check`, `npx tsc --noEmit` on the files, `python -m py_compile`).

## 3. Edit

Go category by category, in this order, because later categories are easier to judge once the noise is gone: R (residue) and C (comments), then V (verbosity) and T (type escapes), then D (defensive), then O (structure), then S (tests).

The user chose aggressive cleanup of defensive code. Inside trust boundaries, remove D findings when types, callers, or the construction of the value show the check cannot fire, and also when you searched for callers and found none that could trigger it. Say in the report which removals rely on "no caller found" rather than on types. Checks at trust boundaries and security checks stay; they are not in the findings list to begin with.

Rules while editing:

- Change only what the chosen findings cover. No drive-by renames, reformatting, or "while I'm here" fixes. If you spot something new, add it to the report as a new finding.
- Do not change the signatures of exported functions, classes, or modules that other packages might import. Inlining or deleting is fine only for code private to the module or package.
- Before deleting a function, file, or export, search the whole repo for its name (including string references, dynamic imports, and config files).
- Files may be deleted or merged when the plan said so. Update every import.
- Deleting test slop: never remove the only test of a behavior. Rewrite it to assert the behavior instead, or keep it.
- When removing a try/catch, keep any real cleanup (`finally`, closing resources) by moving it to `with`, `using`, or `finally` without the catch.
- When the fix for a T1 escape needs real type work that goes beyond the file, leave the escape, add a one-line reason comment only if the project writes such comments, and list it as skipped.

Commit on the deslop branch after each category (`deslop: remove narrating comments`, `deslop: drop redundant null checks`). The plan the user approved named the branch, so these commits are expected, and they let the user revert one category with `git revert`. Do not push.

## 4. Verify

Re-run the baseline checks after each category, or at the end if checks are slow.

- A check that passed before and fails now: find the edit that broke it (the per-category commits make this quick), revert that edit, and list the finding as skipped with the reason.
- Type errors that appear because a removed check was narrowing a type: the check was not slop. Restore it and skip the finding.
- Pre-existing failures that are unchanged: report them, do not touch them.

## 5. Report

Keep it short and follow `voice.md`:

- Branch or worktree name and path, and the commits made.
- What was removed, by category, with counts. Lines before and after for the touched files (`git diff --stat` against the starting commit).
- Check results next to the baseline: `tests 142/142 (was 142/142), tsc clean (was clean), eslint 3 warnings (was 5)`.
- Skipped findings and why, including removals that rely on "no caller found".
- How to take it: `git diff main...deslop/<slug>` to review, merge or `git branch -D` to discard. For a worktree, also `git worktree remove <path>`.
