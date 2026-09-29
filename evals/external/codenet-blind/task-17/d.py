import sys

sys.setrecursionlimit(200005)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
adj = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
depth = [-1] * (N + 1)
path_count = [0] * (N + 1)
edge_count = [0] * (N + 1)
cycle_sum = 0


def dfs(u, p, d):
  parent[u] = p
  depth[u] = d
  for v in adj[u]:
    if v == p:
      continue
    if depth[v] == -1:
      dfs(v, u, d + 1)
    else:
      if depth[v] < depth[u]:
        global cycle_sum
        cycle_sum += 1
        path_count[u] += 1
        path_count[v] -= 1


for _ in range(M):
  a, b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a)
  edges.append((a, b))

dfs(1, 0, 0)

for i in range(1, N + 1):
  if parent[i] != 0:
    edge_count[i] = path_count[i] + path_count[parent[i]]
    if edge_count[i] % 2 != 0:
      print('NO')
      exit()

if cycle_sum == 0:
  if M == N - 1:
    print('YES')
  else:
    print('NO')
else:
  if M == N:
    print('YES')
  else:
    print('NO')
