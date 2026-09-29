import sys
from collections import deque
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
    S, T = map(int, input().split())
    S -= 1; T -= 1
    total = 3 * N
    dist = [-1] * total
    start = S
    dist[start] = 0
    dq = deque([start])
    target = T
    ans = -1
    while dq:
        cur = dq.popleft()
        d = dist[cur]
        node = cur % N
        layer = cur // N
        for v in adj[node]:
            nl = (layer + 1) % 3
            nxt = nl * N + v
            if dist[nxt] == -1:
                dist[nxt] = d + 1
                if nxt == target:
                    ans = dist[nxt] // 3
                    print(ans)
                    return
                dq.append(nxt)
    print(-1)

if __name__ == "__main__":
    main()
