import itertools

def solve_friendships(N, K):
    # Try to construct a graph that satisfies the conditions
    for perm in itertools.permutations(range(1, N+1)):
        graph = [[] for _ in range(N+1)]
        
        # Connect vertices in a simple way
        for i in range(N-1):
            graph[perm[i]].append(perm[i+1])
            graph[perm[i+1]].append(perm[i])
        
        # Compute distances between all pairs
        distances = [[float('inf')] * (N+1) for _ in range(N+1)]
        for v in range(1, N+1):
            distances[v][v] = 0
            queue = [v]
            visited = [False] * (N+1)
            visited[v] = True
            
            while queue:
                u = queue.pop(0)
                for w in graph[u]:
                    if not visited[w]:
                        distances[v][w] = distances[v][u] + 1
                        distances[w][v] = distances[v][w]
                        queue.append(w)
                        visited[w] = True
        
        # Count pairs with distance 2
        dist_2_pairs = sum(1 for i in range(1, N) for j in range(i+1, N+1) if distances[i][j] == 2)
        
        if dist_2_pairs == K:
            # Construct the edges to output
            edges = []
            for i in range(N-1):
                edges.append((perm[i], perm[i+1]))
            
            return len(edges), edges
    
    return -1, []

def main():
    N, K = map(int, input().split())
    
    M, edges = solve_friendships(N, K)
    
    if M == -1:
        print(-1)
    else:
        print(M)
        for u, v in edges:
            print(u, v)

if __name__ == "__main__":
    main()
