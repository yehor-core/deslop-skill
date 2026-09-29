Here's a solution to the problem:

import sys
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    px, py = find(parent, x), find(parent, y)
    if px != py:
        parent[px] = py

def solve(N, M, edges):
    parent = list(range(N+1))
    degree = [0] * (N+1)
    
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
        union(parent, a, b)
    
    # Check if graph is connected
    root = find(parent, 1)
    for i in range(1, N+1):
        if find(parent, i) != root:
            return "NO"
    
    # Check if graph becomes a tree
    odd_degree_count = sum(1 for d in degree[1:] if d % 2 == 1)
    return "YES" if odd_degree_count == 0 or odd_degree_count == 2 else "NO"

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(solve(N, M, edges))

if __name__ == "__main__":
    main()
