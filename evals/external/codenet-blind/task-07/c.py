import sys

sys.setrecursionlimit(200000)

N, K = map(int, sys.stdin.readline().split())
MOD = 1000000007

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

ans = K
cnt = [0] * (N + 1)

def dfs(u, p):
    cnt[u] = 1
    for v in adj[u]:
        if v == p:
            continue
        dfs(v, u)
        cnt[u] += cnt[v]

dfs(1, 0)

ans = K
for i in range(2, N + 1):
    if cnt[i] < cnt[1] - cnt[i]:
        ans = (ans * (K - 1)) % MOD
    else:
        ans = (ans * (K - 2)) % MOD

print(ans)
