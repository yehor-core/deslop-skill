```python
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
H, W = map(int, input().split())
S = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, d):
  dist[x][y] = d
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (
        0 <= nx < H
        and 0 <= ny < W
        and S[nx][ny] != S[x][y]
        and dist[nx][ny] == -1
    ):
      dfs(nx, ny, d + 1)


ans = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == '#' and dist[i][j] == -1:
      dfs(i, j, 0)
for i in range(H):
  for j in range(W):
    if S[i][j] == '.' and dist[i][j] != -1:
      ans += dist[i][j]
print(ans)
```
