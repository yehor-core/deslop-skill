# Expected findings: ts-react-profile

## Bugs, not slop
- `ProfileCard.tsx` effect: deps are `[]` with the exhaustive-deps rule disabled, so changing `userId` never refetches.
- `error` state is never set; the catch only `console.log`s, so a failed fetch renders "Joined " with an empty card. Hidden by D1.
- `{/* ... rest of the card unchanged ... */}` (R7): elided JSX may be real missing content; report as possible bug.
- `api.ts`: `API_KEY = "YOUR_API_KEY_HERE"` and `api.example.com` placeholders on a live path (R3).

## Slop
- C3 chat preamble on line 1.
- O3 unused props `compact`, `theme`, `onError` (component is exported: report only; props interface is not a function signature, but default-export component props count as public API, so do not remove without user choice).
- O1 `useLoadingState` hook wrapping one `useState`.
- T1 `data as any`; eslint-disable (T1).
- D1 catch that only logs.
- React: `useMemo` around `profile?.name ?? ""`, `useCallback` with no memoized consumer; `handleClick` logs only (R1).
- V5 `moment` for one date format (platform `toISOString().slice(0, 10)` or `Intl.DateTimeFormat`).
- R2 commented-out avatar code; C1 narrating comments; C2 component docstring.

## Must not flag
- `if (!res.ok) throw ...` in `api.ts` (network boundary).
