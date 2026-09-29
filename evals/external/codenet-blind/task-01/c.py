from collections import deque

def solve(H, W, grid):
    def is_valid(x, y):
        return 0 <= x < H and 0 <= y < W

    def is_black(x, y):
        return grid[x][y] == '#'

    def bfs(start_x, start_y, color):
        visited = [[False] * W for _ in range(H)]
        count = 0
        queue = deque([(start_x, start_y, color, 0)])
        visited[start_x][start_y] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, prev_color, seq_len = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    if (prev_color == 0 and is_black(nx, ny)) or \
                       (prev_color == 1 and not is_black(nx, ny)):
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            if (color == 0 and not is_black(nx, ny)) or \
                               (color == 1 and is_black(nx, ny)):
                                count += 1
                            queue.append((nx, ny, 1 - prev_color, seq_len + 1))

        return count

    total_paths = 0
    for x in range(H):
        for y in range(W):
            if is_black(x, y):
                total_paths += bfs(x, y, 0)
            else:
                total_paths += bfs(x, y, 1)

    return total_paths

def main():
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    print(solve(H, W, grid))

if __name__ == "__main__":
    main()
