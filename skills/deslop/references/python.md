# Python slop

Shapes of the general patterns that show up in Python. IDs refer to `patterns.md`. Before flagging, check `pyproject.toml` (mypy/pyright strictness, ruff rules, target version) and two or three neighboring modules for the house style.

## Defensive overkill

- **D1/D2** `try: ... except Exception as e: logger.error(f"Error in {func}: {e}"); return None` around a whole function. `except Exception: pass`. `raise Exception("Failed to process")` inside `except`, which loses the type (if a wrap is needed, `raise NewError(...) from e`).
- **D3** `if not isinstance(items, list): raise TypeError(...)` on an annotated `items: list[Item]` in internal code; `if x is None: raise ValueError` on a non-Optional parameter; `assert isinstance(...)` sprinkled at the top of private functions.
- **D4** `dict.get("key", {})` or `getattr(obj, "attr", None)` on keys and attributes that always exist; `or []` after a function that always returns a list; `os.environ.get("DATABASE_URL", "sqlite:///default.db")` that silently runs against the wrong database.
- **D5** Re-validating a pydantic model or dataclass by hand after it was constructed.
- **D6** `for attempt in range(3):` around local file or in-memory work.
- **D7** `logger.info(f"Starting {func_name}")` / `logger.info("Done")` pairs; `print(f"✅ ...")`.

## Over-engineering

- **O2** `class BaseProcessor(ABC)` with one subclass; `Protocol` with one implementer and no fakes in tests; a `ProcessorFactory.create()` that returns one class.
- **O4** Classes holding only `@staticmethod`s; `class Config:` with only class attributes used as a namespace where a module works; a class with `__init__` and one method, instantiated once (use a function).
- **O3** `**kwargs` passed through three layers and never read; keyword arguments with defaults no caller overrides.
- **O7** A `constants.py` with one value; `Enum` for two strings used in one place when the project uses `Literal`.
- **O8** `utils/__init__.py` re-exporting one function; `example_usage.py`, `demo.py`, `if __name__ == "__main__":` demo blocks in library modules.
- Dataclass or pydantic model wrapping a single field that is passed straight through.

## Verbosity

- **V2** `if cond: return True else: return False`; `True if x else False`; `== True`, `== False`, `is True`.
- **V3** `result = []` / `for` / `append` where a comprehension fits; `for i in range(len(xs))` when only `xs[i]` is used (use `for x in xs` or `enumerate`).
- **V1** `result = compute(); return result`.
- **V5** Hand-written flatten, chunk, retry, or path joining where `itertools`, `more_itertools` (if already a dependency), `tenacity` (if already used), or `pathlib` covers it; manual `open`/`close` without `with`.
- `len(x) > 0` / `len(x) == 0` where the project uses truthiness (low severity; PEP 8 prefers truthiness for sequences).
- Imports inside functions without a reason such as a circular import or an optional heavy dependency (R6 / style).
- f-strings in logging calls where the project uses `%s` lazy formatting.

## Type escapes

- **T1** `# type: ignore` without an error code or reason, `cast(Any, ...)`, `Any` in new signatures, `# noqa` without a rule code.
- **T2** `assert x is not None` repeated before every use instead of narrowing once.
- Type annotations on every local variable (`count: int = 0`) where the project annotates only signatures.

## Tests (pytest, unittest)

- **S1** `mock.assert_called_once_with(...)` as the only check, with the return value ignored.
- **S2** `assert func is not None`, `assert callable(func)`, `assert isinstance(Model(a=1), Model)`.
- **S3** Tests that a dataclass stores its fields or that pydantic rejects the wrong type.
- **S4** Ten near-identical test functions where one `@pytest.mark.parametrize` covers them; parametrize tables whose rows all hit the same branch.
- Fixtures that return a constant and are used once; `unittest.TestCase` classes in a project that uses plain pytest functions.

## Residue

- **R1** `print(...)`, `pprint`, `breakpoint()`, `import pdb`.
- **R3** `pass  # TODO: implement`, `return {}  # placeholder` on a live path; `NotImplementedError` in a method that is called.
- **R4** Unused imports and variables (ruff F401/F841 catch these if enabled).
