import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                dq = deque()
                visited[i][j] = True
                dq.append((i,j))
                b = 0
                w = 0
                if S[i][j] == '#':
                    b += 1
                else:
                    w += 1
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and S[nx][ny] != S[x][y]:
                            visited[nx][ny] = True
                            if S[nx][ny] == '#':
                                b += 1
                            else:
                                w += 1
                            dq.append((nx, ny))
                ans += b * w
    print(ans)

if __name__ == "__main__":
    main()
