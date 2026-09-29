# Slop score

A score from 0 to 10 per file and overall, with a one-line verdict. It measures how much of the code is slop, not who wrote it. Never say or imply "this was written by AI"; say how much of it a careful maintainer would delete.

## How to get the number

Estimate two things for each file (for a diff: the changed lines only):

1. **Removable share**: the fraction of lines the chosen cleanup could delete or collapse without changing behavior. Count comment lines, wrapper bodies, redundant checks, dead code.
2. **Harm**: whether any finding hides errors or misleads the reader. That means high-severity D1, D2, D4, T1, S1, S2, or R3.

Start from the removable share, then adjust:

| Removable share | Base score |
| --- | --- |
| under 5% | 0 to 1 |
| 5% to 15% | 2 to 3 |
| 15% to 30% | 4 to 5 |
| 30% to 50% | 6 to 7 |
| over 50% | 8 to 10 |

- Add 1 (or 2 when there are several) if findings hide errors or mislead: swallowed exceptions, fallbacks over impossible states, tests that cannot fail.
- Subtract 1 if every finding is low severity.
- Clamp to 0..10.

Overall score: weight each file's score by its line count (changed lines for a diff), round to an integer.

Show the removable share next to the score so the user can see where the number comes from: `6/10, about 35% of lines removable`.

## Verdict lines

Pick the band's line and make it specific to the code. Do not copy the examples word for word.

- **0 to 1**: clean. "Nothing worth cleaning; two comments restate the code."
- **2 to 3**: light. "Mostly fine. A few narrating comments and one pointless try/catch."
- **4 to 5**: noticeable. "About a quarter is noise; the logic is easy to find once the wrappers are gone."
- **6 to 7**: heavy. "More wrapper than logic. The error handling hides failures from callers."
- **8 to 10**: mostly slop. "The behavior fits in about 40 lines out of 200."

## Per-file table

When there is more than one file, show a compact table sorted by score:

```
file                         score  removable  top patterns
src/services/userService.ts  7      ~40%       D2 x4, O2, C1 x12
src/utils/format.ts          2      ~8%        C1 x3
```

Files with a score of 0 are listed in one line at the end ("clean: a.ts, b.ts"), not in the table.
