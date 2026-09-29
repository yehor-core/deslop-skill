from collections import defaultdict, deque

def solve(N, K, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def check_neighborhood_colors(node, colors):
        color_nodes = defaultdict(list)
        color_nodes[colors[node-1]].append(node)

        queue = deque([(node, 0)])
        visited = {node}

        while queue:
            curr, dist = queue.popleft()
            if dist >= 2:
                break

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist+1))
                    if dist < 2:
                        if colors[neighbor-1] in color_nodes:
                            return False
                        color_nodes[colors[neighbor-1]].append(neighbor)

        return True

    def dfs(node, parent):
        ways = 1
        MOD = 10**9 + 7
        colors_used = set()

        for child in graph[node]:
            if child == parent:
                continue

            child_ways = 0
            for color in range(1, K+1):
                if color in colors_used:
                    continue

                valid_coloring = True
                colors = [0] * N
                colors[node-1] = color
                colors[child-1] = color

                for neighbor in graph[child]:
                    if neighbor != node and neighbor != parent:
                        for c in range(1, K+1):
                            if c != color:
                                colors[neighbor-1] = c
                                if check_neighborhood_colors(neighbor, colors):
                                    valid_coloring = True
                                    break
                        if not valid_coloring:
                            break

                if valid_coloring:
                    child_ways += dfs(child, node)

            ways = (ways * child_ways) % MOD
            colors_used.add(color)

        return ways

    return dfs(1, 0)

def main():
    N, K = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    print(solve(N, K, edges))

if __name__ == "__main__":
    main()
