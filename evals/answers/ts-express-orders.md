# Expected findings (hidden from the skill under test)

Do not pass this file to the skill. It is the answer key for graders.

## Bugs, not slop
- `routes/orders.ts` GET handler: `orderService.getOrder(...)` is not awaited, so `order` is a Promise, never falsy; the 404 never fires and the response serializes `{}`.

## Slop
- `routes/orders.ts`: T3 widen-then-assert (`Record<string, unknown>` then `as unknown as CreateOrderInput`); D1 catch-log-then-`next(error)` in both handlers (Express already forwards via `next`, the log duplicates the error middleware); R1/C6 emoji `console.log`; C1 narrating comments; C2 route docstrings restating the path.
- `services/orderService.ts`: D5 re-validation of fields zod already checked (whole block of ifs); D3 `if (!input)`; V3 manual sum loop (use `reduce`); D6 retry around an in-memory save; C2 docstrings; O3 optional `repository` constructor param is fine for tests, NOT slop if tests inject it (none do here: low).
- `repositories/orderRepository.ts`: D5 third validation layer; D3 null/undefined/"" check on `id: string`; D4 `order ?? undefined`; C2 docstrings.

## Must not flag
- The zod schema itself (trust boundary).
- `next(error)` as the error path (it is the Express convention; only the extra log is slop).
