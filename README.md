# deslop

[![skills.sh installs](https://skills.sh/b/yehor-core/deslop-skill)](https://skills.sh/yehor-core/deslop-skill)

deslop is a skill for coding agents that reviews AI-written code. It tells you what the code does, shows which parts are slop and why, scores it from 0 to 10, and removes only the parts you pick.

Slop here means code that adds lines without adding behavior: comments that narrate the next line, try/catch blocks that hide errors, checks the types already guarantee, interfaces with one implementation, options nobody passes, tests that cannot fail. The skill judges code against the rest of your codebase. The score says how much of the code is slop; it does not guess whether a model wrote it, since people write slop too.

## Example

Before:

```python
def load_config(path: str) -> AppConfig:
    """
    Load the application configuration.

    Args:
        path (str): Path to the config file.

    Returns:
        AppConfig: The configuration.
    """
    try:
        # Validate the path
        if path is None or not isinstance(path, str):
            raise ValueError("Path must be a string")
        logger.info(f"Loading config from {path}")
        # Read the file
        with open(path) as f:
            data = json.load(f)
        logger.info("✅ Config loaded successfully")
        return AppConfig(**data)
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        # Fall back to default config
        return AppConfig(database_url="sqlite:///default.db")
```

deslop's explanation:

> `load_config` reads a JSON file into `AppConfig`. If anything goes wrong, including a typo in the file, it logs one line and returns a config that points at `sqlite:///default.db`, so the app starts against the wrong database.
>
> 8/10, about 80% of lines removable.
>
> 1. [D4] `config.py:21-24` | high | catch-all returns a default config | a broken config file looks like a working one
> 2. [D3] `config.py:12-14` | med | `isinstance` check on `path: str` | the type already guarantees it
> 3. [C2] `config.py:2-10` | med | docstring repeats the signature
> 4. [D7] `config.py:15, 19` | med | log lines before and after a file read

After you pick "Everything":

```python
def load_config(path: str) -> AppConfig:
    with open(path) as f:
        return AppConfig(**json.load(f))
```

## Install

```bash
npx skills add yehor-core/deslop-skill --skill deslop --global --agent claude-code
```

Swap `claude-code` for `codex`, `cursor`, or another agent the [Skills CLI](https://github.com/vercel-labs/skills) supports, or use `--agent '*'` for all of them. Leave off `--global` to install the skill only in the current project.

The skill works best in Claude Code, where its questions show up as clickable menus. Other agents get the same questions as numbered lists.

## Usage

Point it at code:

```
/deslop src/services/userService.ts
/deslop src/api
/deslop 482            # a pull request, via the gh CLI
/deslop diff           # your branch and uncommitted changes
/deslop project
```

Or ask in plain language:

```
Does this look AI-written? src/sync.ts
Clean up the slop in the last commit
Почисти этот код от слопа: [paste]
```

Add `--clean` to go straight to the cleanup menu with a short explanation.

## How it works

1. deslop reads the code once and tells you what it does and where its size comes from. Real bugs it notices, such as a missing `await`, go in a separate list and stay out of the cleanup.
2. If you ask for details, you get every finding with `file:line`, a short quote, and the reason it is slop, grouped by category, with a 0 to 10 score per file and overall.
3. A menu asks what to clean: everything, nothing, or a set of categories. You can then drop individual findings from the selection.
4. You see the plan and a before/after for the largest edits. Nothing changes until you confirm.
5. deslop works on a new branch, or in a git worktree if you have unrelated uncommitted changes. It runs your tests, type checker, and linter before and after, reverts any edit that breaks a check that used to pass, and commits each category separately so you can undo one with `git revert`.

Validation at trust boundaries (user input, HTTP, files, env vars), security checks, error handling with a real recovery, comments that explain why, and the signatures of exported functions stay as they are. The only test of a behavior is never deleted.

Explanations follow writing rules adapted from [Humanizer](https://github.com/blader/humanizer), so the review of AI slop does not read like AI slop.

The patterns are tuned for TypeScript/JavaScript and Python, and the general ones apply to any language.
