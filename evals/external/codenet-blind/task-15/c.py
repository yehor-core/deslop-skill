from itertools import combinations

def solve():
    N = int(input())
    sardines = []
    for _ in range(N):
        A, B = map(int, input().split())
        sardines.append((A, B))
    
    MOD = 10**9 + 7
    total_ways = 0
    
    for r in range(1, N + 1):
        for subset in combinations(range(N), r):
            valid = True
            for i, j in combinations(subset, 2):
                A1, B1 = sardines[i]
                A2, B2 = sardines[j]
                if A1 * A2 + B1 * B2 == 0:
                    valid = False
                    break
            if valid:
                total_ways += 1
    
    print(total_ways % MOD)

solve()
