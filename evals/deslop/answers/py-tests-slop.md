# Expected findings: py-tests-slop

## Bugs, not slop
- `test_loyalty_cap` is skipped as "flaky" but is deterministic; it is the only test of the 5-year cap (S5). Unskip, do not delete.
- `test_welcome_coupon` asserts `> 0` instead of `== 1000` (S5 weakened assertion).

## Slop
- S2 `test_discount_cents_exists`, `test_module_has_cart` (cannot fail meaningfully).
- S3 `test_cart_creation` tests the dataclass machinery.
- S2 `test_discount_matches_formula` re-implements the formula in the test (tautological).
- S1 `test_discount_calls_min` asserts an implementation detail via mock of a builtin.
- S4 `test_discount_zero_years` .. `test_discount_four_years`: collapse into one `@pytest.mark.parametrize`.
- C2 module docstring ("comprehensive", "thoroughly") and per-test docstrings restating the name.

## Must not delete
- Coverage of: zero years, per-year rate, 5-year cap, WELCOME10 coupon. After cleanup, each must still have a test with an exact expected value.
