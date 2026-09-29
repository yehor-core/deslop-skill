# TypeScript / JavaScript slop

Shapes of the general patterns that show up in TS/JS. IDs refer to `patterns.md`. Before flagging, check `tsconfig.json` (is `strict` on?), the lint config, and two or three neighboring files for the house style.

## Defensive overkill

- **D3** Runtime checks on typed values under `strict`: `if (typeof name !== "string") throw ...` when `name: string`; `if (!items || !Array.isArray(items))` on `items: Item[]`; `if (user === null || user === undefined)` on a non-nullable `User`. In plain JS or with `strict: false`, these may be the only safety net; lower the severity.
- **D4** `?? ""`, `?? []`, `?? 0`, `|| {}` on non-optional properties; `?.` chains on values that cannot be nullish (`config?.db?.host` after `config` was validated by zod); `.catch(() => [])` on a fetch whose failure the caller needs to know about.
- **D1/D2** `async` functions whose whole body is `try { ... } catch (error) { console.error("Error in X:", error); throw error; }`; `catch (e: any)` followed by `throw new Error("Failed to X")`, which drops the original error (if kept, use `{ cause: e }`).
- **D2** Express/Next handlers each wrapped in their own try/catch when the app already has error middleware or an error boundary.
- **D5** Validating a zod-parsed object again by hand, field by field.
- **D7** `console.log("✅ Successfully fetched users:", users.length)` and friends.

## Over-engineering

- **O2** `interface IUserRepository` + `class UserRepository implements IUserRepository` with no second implementation and no test double; `createXFactory()` returning one class.
- **O3** Options objects with optional fields nobody passes; generic type parameters that are only ever one type (`function load<T = Config>(...)` called once with `Config`).
- **O4** `class StringUtils { static capitalize(...) }`; a class with a constructor and one method, instantiated once.
- **O8** `index.ts` barrels that re-export a single file; `types.ts` holding one type used in one file.
- **O7** `enum Status { Active = "active", Inactive = "inactive" }` used once where a string union matches the project; `const MAX_RETRIES = 3` exported from `constants.ts` and used in one place.
- React: `useCallback`/`useMemo` around cheap values with no memoized child consuming them; a custom hook that wraps one `useState`; prop-drilling helpers for one level.

## Verbosity

- **V2** `return x ? true : false`, `if (cond) return true; return false;`, `!!` on something already boolean.
- **V3** `for` loops with `push` where `map`/`filter` reads cleaner; `reduce` used to build an array that `map` would build.
- **V1** `const response = await fetch(url); return response;`.
- **V5** Hand-written `sleep`, `deepClone` (use `structuredClone`), `groupBy` (use `Object.groupBy` if the target supports it), `uuid` (use `crypto.randomUUID`), or a copy of a util already in `src/lib`.
- `async` on functions that never `await`; `return await` outside try blocks; `new Promise((resolve) => resolve(x))`; `.then()` chains mixed with `await` in the same function.

## Type escapes

- **T1** `as any`, `: any` parameters, `as unknown as X`, `// @ts-ignore`, `// eslint-disable-next-line @typescript-eslint/no-explicit-any` added in the change.
- **T2** `obj!.field!` chains; `as NonNullable<...>` casts where a single narrowing `if` would do.
- Redundant annotations the project does not use: `const count: number = 0`, `(): void =>` on every arrow when the house style relies on inference.

## Tests (jest, vitest)

- **S1** `expect(mockFn).toHaveBeenCalledWith(...)` as the only assertion, where `mockFn` is the unit under test's own dependency and the result is ignored.
- **S2** `expect(fn).toBeDefined()`, `expect(typeof fn).toBe("function")`.
- **S3** Tests that a TS interface "has" properties by constructing an object literal.
- `describe` blocks with one `it` each, nested three deep, for a single function.
- `beforeEach` resetting mocks that `restoreMocks: true` in the config already resets.

## Residue

- **R1** `console.log`, `console.debug`, `debugger`.
- **R3** `// TODO: replace with real API call` above a hardcoded array.
- **R4** Unused imports (the linter usually catches these; mention only if lint is not set up).
