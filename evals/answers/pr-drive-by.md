# Expected findings: pr-drive-by (diff review)

The PR's stated purpose is one typo. Only `"Pasword" -> "Password"` belongs to it.

## Bugs, not slop
- `templateCache` caches password reset bodies keyed by user and link: reset links are secrets and single-use; caching them in process memory for up to 500 entries is a security smell and pointless (each link is unique, so the cache never hits).
- `sendPasswordReset` now swallows send failures (D1): callers can no longer tell the user the email failed.
- New dependency `lru-cache` added for a one-typo PR.

## Slop
- R5 unrequested feature: cache, `TemplateOptions` (O3: `locale`, `escapeHtml` unused; `useCache` only read once).
- O3/V8 new optional `options` param on an exported function: it is new in this PR, so removing it restores the original signature (allowed).
- D3/D4 `if (!user || !user.firstName)` fallback to "Hi there" on a typed non-null `User`.
- C1/C2 comment and docstring noise.
- R6 drive-by reformat of `send.ts` (quotes, semicolons) unrelated to the typo; hides the real try/catch change in review.

## Expected recommendation
Keep only the typo fix; split any formatting into its own PR.
