```python
from collections import defaultdict, deque

def solve(N, M, edges, S, T):
    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # BFS to find minimum ken-ken-pa count
    queue = deque([(S, 0, 0)])
    visited = set()
    
    while queue:
        node, steps, moves = queue.popleft()
        
        if steps == 3 and node == T:
            return moves
        
        # Pruning: avoid revisiting same state 
        state = (node, steps)
        if state in visited:
            continue
        visited.add(state)
        
        # Try all possible edges from current node
        for next_node in graph[node]:
            if steps < 3:
                queue.append((next_node, steps + 1, moves))
            elif steps == 3:
                queue.append((next_node, 1, moves + 1))
    
    return -1

def main():
    N, M = map(int, input().split())
    
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    S, T = map(int, input().split())
    
    result = solve(N, M, edges, S, T)
    print(result)

if __name__ == "__main__":
    main()
```
