# deslop

A Claude Code plugin with one skill, `deslop`, that explains AI slop in code to a reviewer, scores it, and removes the parts the user picks.

Tuned for TypeScript/JavaScript and Python; the general patterns work for any language.

## Flow

1. You point it at code: a PR number, a diff, a file, a folder, the whole project, or a pasted snippet.
2. It explains what the code does and where the bulk comes from, then asks whether to show the slop.
3. It lists every finding with `file:line`, groups them by category, and scores each file from 0 to 10.
4. A menu asks what to clean: everything, nothing, or by category, with an optional per-finding pass.
5. It shows the plan and before/after for the largest edits, and waits for confirmation.
6. It cleans on a separate branch or worktree, runs tests, type check, and lint before and after, rolls back any edit that broke a check, and commits per category.

## Install

```bash
claude plugin marketplace add /path/to/explain-ai-code-skill
claude plugin install deslop@deslop
```

Or try it without installing: `claude --plugin-dir /path/to/explain-ai-code-skill`.

Then run `/deslop:deslop 123` for a PR, `/deslop:deslop src/services`, or just ask "does this look AI-written?".

## Layout

```
.claude-plugin/         plugin and marketplace manifests
skills/deslop/
  SKILL.md              the workflow, kept short
  references/
    voice.md            how explanations should read (adapted from Humanizer)
    patterns.md         slop catalog with IDs, severity, and exceptions
    typescript.md       TS/JS shapes of the patterns
    python.md           Python shapes of the patterns
    scoring.md          0-10 score rubric
    cleanup.md          branch/worktree, baseline checks, editing rules, report
evals/                  test material, not loaded by the skill (see evals/README.md)
  evals.json            15 test prompts
  fixtures/             hand-written sloppy and clean TS/Python scenarios
  answers/              answer keys for the fixtures
  external/             labeled cases from stopslop, anti-slop, and a blind CodeNet set
  scripts/              importers and a scorer for labeled runs
```

Reference files load only at the step that needs them, so the agent's context stays small.

## Defaults worth knowing

- Defensive code is cleaned aggressively inside trust boundaries. Checks at boundaries (user input, network, files, env) and security checks are never flagged.
- Signatures of exported functions are never changed.
- Test slop may be deleted, but never the only test of a behavior.
- The score measures slop, not authorship. Humans write slop too.

## Credits

`references/voice.md` adapts parts of [Humanizer](https://github.com/blader/humanizer) by Siqi Chen (MIT), which is based on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Eval material under `evals/external/` comes from [stopslop](https://github.com/mgiovani/stopslop) (MIT), [anti-slop](https://github.com/dmmulroy/anti-slop) (MIT), and the [ai-code-detection](https://huggingface.co/datasets/serafeimdossas/ai-code-detection) dataset (MIT); each folder keeps its license. Slop categories draw on existing deslop prompts from [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow/blob/main/skills/deslop/SKILL.md), Sentry's deslop skill, and [Jose Casanova's AI code slop reviewer](https://www.josecasanova.com/prompts/ai-code-slop-reviewer).
