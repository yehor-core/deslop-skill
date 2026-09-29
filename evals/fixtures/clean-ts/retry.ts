// Retries only on network errors and 5xx responses. 4xx means the request
// itself is wrong, so repeating it would just hit the rate limit faster.
export async function fetchWithRetry(
  url: string,
  init: RequestInit = {},
  attempts = 3,
): Promise<Response> {
  let lastError: unknown;
  for (let i = 0; i < attempts; i++) {
    try {
      const res = await fetch(url, init);
      if (res.status < 500) return res;
      lastError = new Error(`HTTP ${res.status} from ${url}`);
    } catch (err) {
      lastError = err;
    }
    // Backoff: 200ms, 400ms, 800ms...
    await new Promise((r) => setTimeout(r, 200 * 2 ** i));
  }
  throw new Error(`fetch failed after ${attempts} attempts: ${url}`, { cause: lastError });
}

export function parseLimit(raw: string | null): number {
  // Query string comes from the client, so it is untrusted.
  const n = Number(raw);
  if (!Number.isInteger(n) || n < 1) return 20;
  return Math.min(n, 100);
}
