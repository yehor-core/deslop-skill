# Expected findings: ts-duplicate-helpers (project scope)

## Slop
- V5 project-level: three date formatters (`utils/date.ts formatDate`, `lib/formatters.ts formatDateString`, `components/InvoiceRow.tsx toDisplayDate`).
  They are NOT identical: `toDisplayDate` uses `toISOString()` (UTC), the other two use local time. A good answer says so before proposing a merge, and asks or keeps behavior.
- V5 `deepClone` via JSON (use `structuredClone`); `InvoiceRow` clones the invoice via JSON only to read `id` (dead work; also turns Dates into strings).
- V2 `isOverdue` if/else returning booleans.
- D3/D4 `formatDateString` accepts `Date | string | number | null | undefined` and returns "" for bad input: check callers (none in project), speculative widening (O3) plus a fallback that hides bad dates (D4).
- C2 docstrings restating names; C1 "Helper function to..." comments.

## Must not flag
- `formatCurrency` (uses Intl correctly).
- `daysBetween`.
