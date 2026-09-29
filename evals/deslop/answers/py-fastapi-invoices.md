# Expected findings: py-fastapi-invoices

## Bugs, not slop
- `from fastapi_utils.cbv import cbv_router_factory  # noqa: F401`: hallucinated import (no such symbol), silenced with noqa; app fails to import if the package is missing.
- `create_invoice` catch-all returns `{"id": None, "total_cents": 0}` with HTTP 200 on any failure: clients think the invoice was created.
- `STRIPE_API_KEY = "sk_test_YOUR_KEY_HERE"`: placeholder secret (R3); security note.
- `customer_email: str` accepts any string (EmailStr missing): a boundary gap. Mention as a risk, do not "fix" in cleanup.

## Slop
- C2/C? module docstring with sales language ("robust", "scalable", "leveraging", "seamless").
- V8/O3 `calculate_total` has three bool flags that do nothing; called as `calculate_total(items, False, False, False)`. Not exported via __all__, module-level in an app: private enough to remove flags.
- V3 manual sum loop (use `sum(...)`).
- C2 docstring restating the signature.
- D5 `validate_invoice` re-checks what pydantic already enforced (min_length, gt=0, types); whole function is removable, along with the 400 branch.
- D2 whole-function try with generic except; `except HTTPException: raise` exists only because of the broad except.
- V1 `result = {...}; return result`.
- D7 log noise ("created successfully").
- T? `Optional[...]` return on `get_invoice` that never returns None (low).

## Must not flag
- The 404 in `get_invoice`.
- Pydantic `Field` constraints (boundary validation).
