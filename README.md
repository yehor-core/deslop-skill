# skills

[![skills.sh installs](https://skills.sh/b/yehor-core/skills)](https://skills.sh/yehor-core/skills)

Skills for coding agents: Claude Code, Codex, Cursor, and anything else the [Skills CLI](https://github.com/vercel-labs/skills) supports.

| Skill | What it does |
| --- | --- |
| [deslop](skills/deslop) | Explains AI slop in code, scores it from 0 to 10, and removes the parts you pick |

## Install

One skill:

```bash
npx skills add https://github.com/yehor-core/skills --skill deslop
```

Every skill in this repo:

```bash
npx skills add https://github.com/yehor-core/skills
```

The CLI asks which agents to install for. Add `--agent <name>` to skip the prompt and `--global` to install for all your projects instead of only the current one. Each skill's README covers usage.

## Layout

```
skills/<name>/     the skill itself: SKILL.md, references/, LICENSE, README.md
evals/<name>/      test prompts, fixtures, and scripts for that skill; never installed
```

The Skills CLI copies only `skills/<name>/`, so anything a skill needs at runtime lives there, including its LICENSE when it adapts third-party text. A new skill gets its own `skills/<name>/` folder and, if it has tests, `evals/<name>/`.
