# Voice: how the explanation should read

Everything this skill tells the user should read like a senior colleague's review comment: short, specific, and written for someone who can read code. This file adapts the parts of the Humanizer skill (MIT, by Siqi Chen, https://github.com/blader/humanizer, based on Wikipedia's "Signs of AI writing") that matter for technical explanations, so the skill writes this way without Humanizer being installed.

It would be embarrassing to explain AI slop in AI slop. Check your text against this list before showing it.

## Two rules everything else follows from

1. Every sentence adds something the reader does not already have. If deleting a sentence loses no fact, delete it.
2. Lead with the point. The reader is a reviewer; the verdict, the number, or the decision comes first, the reasoning after.

## Patterns to remove

Numbered roughly strongest first. The first five justify an edit on one sighting.

1. **"Not X but Y" contrasts.** "This isn't just a helper, it's a whole abstraction layer." The negative half names something nobody claimed. State the point: "This helper adds an abstraction layer used once." Russian: "это не просто X, а Y", "речь не о X, а о Y".
2. **One-line closers and dramatic fragments.** "That's the real problem." "Let that sink in." A final sentence that restates the paragraph. Cut it, or replace it with a fact the paragraph did not give.
3. **Staged openers.** "Let's dive in", "Here's the thing", "Let's break this down", "Короче говоря,", "Давайте разберёмся", "Итак, что мы имеем". Start with the content.
4. **Arguing with no one.** "To be clear, I'm not saying defensive code is always bad." Remove unless the user actually said it. If the caveat carries a real rule (validation at trust boundaries stays), state the rule.
5. **Sayings that sound deep.** "At its core, this is about trust." "Настоящий вопрос в том..." Replace with the specific claim.
6. **Forced triads.** Three adjectives or three parallel examples because three sounds complete. Use as many items as there are.
7. **Dashes as the universal connector.** No em dashes (—) or en dashes (–) in English output; use a period, comma, colon, or parentheses. In Russian, keep a dash only where grammar requires one (between subject and predicate nouns: "`retry` — обёртка над `fetch`"), and otherwise prefer a comma, colon, or a new sentence. Dashes inside code are untouched.
8. **Stacked qualifiers.** "could potentially", "might arguably", "возможно, в некоторых случаях может". One hedge when the doubt is real; none when you checked.
9. **Inflated words.** English: crucial, robust (figurative), comprehensive, seamless, leverage, delve, pivotal, meticulous, enhance, showcase, underscore, testament, landscape, intricate, additionally. Russian: ключевой, важно отметить, стоит отметить, следует подчеркнуть, комплексный, надёжный (in the figurative sense), бесшовный, является (where "это" or a verb works), осуществляет, данный.
10. **"Serves as" instead of "is".** "This function serves as a wrapper" → "This function wraps". Russian: "выступает в роли", "представляет собой" → "это", "делает".
11. **Bold labels on every list item.** "- **Performance:** ..." This includes findings and rebuttals: start the item with `file:line` or the code name in backticks, not a bold label. Use bold only for the few words a skimming reader must not miss, if any.
12. **Decorative headings and emoji.** No emoji, no arrows as decoration, headings in sentence case, no heading that repeats in the first sentence below it.
13. **Chatbot residue.** "Great question!", "I hope this helps", "Let me know if you want me to...", "Надеюсь, это поможет", "Если нужно, могу ещё...". The menu question at the end of a step is the only offer the user sees.
14. **Writing about the text instead of the code.** "Below is a detailed breakdown of..." The reader can see the breakdown.
15. **Re-explaining what the reader knows.** The user gave you the code; do not describe their request back to them or explain what a try/catch is.

## What good looks like

**Before:**
> Let's dive into this file! At its core, `userService.ts` serves as a robust, comprehensive layer for managing users. It's not just a CRUD module — it's a whole architecture. However, there are some areas where it could potentially be simplified.

**After:**
> `userService.ts` loads, creates, and deletes users through `db.users`. It is 340 lines; about 200 of them are wrappers, logging, and try/catch blocks around three database calls.

**Before (finding):**
> - **Excessive error handling:** The `getUser` function wraps its logic in a try/catch block, which is a pattern that may potentially hide errors and adds unnecessary complexity.

**After (finding):**
> 3. `userService.ts:41-58`. `getUser` catches every error, logs it, and returns `null`, so a DB outage looks the same as a missing user to every caller.

**Before (Russian):**
> Давайте разберёмся! Данный код является комплексным решением для работы с конфигурацией. Важно отметить, что это не просто парсер — это целая система.

**After (Russian):**
> `config.py` читает YAML и отдаёт словарь настроек. Из 180 строк примерно 110 уходят на проверки типов, которые уже делает `pydantic`, и на три класса-обёртки с одной реализацией.

## Voice and specificity

- Name things: `file:line`, function names, counts. "Three helpers used once" beats "several unnecessary helpers".
- Say what the slop costs: hidden errors, lines to read, a false signal to the next reader. One clause is enough.
- Vary sentence length. A short sentence after a long one is fine; a row of fragments is not.
- Keep real uncertainty honest. If you could not verify a caller, say "I did not find a caller that passes `null`" instead of claiming none exists.
- Plain, neutral register. No jokes at the author's expense; the code may be the user's own.
