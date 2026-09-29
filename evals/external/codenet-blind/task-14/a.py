from itertools import combinations

def solve(N, M, X, costs, books):
    min_cost = float('inf')
    
    for r in range(1, N + 1):
        for combo in combinations(range(N), r):
            understanding = [0] * M
            current_cost = 0
            
            for idx in combo:
                current_cost += costs[idx]
                for j in range(M):
                    understanding[j] += books[idx][j]
            
            if all(level >= X for level in understanding):
                min_cost = min(min_cost, current_cost)
    
    return min_cost if min_cost != float('inf') else -1

def main():
    N, M, X = map(int, input().split())
    costs = []
    books = []
    
    for _ in range(N):
        book_info = list(map(int, input().split()))
        costs.append(book_info[0])
        books.append(book_info[1:])
    
    result = solve(N, M, X, costs, books)
    print(result)

if __name__ == "__main__":
    main()
