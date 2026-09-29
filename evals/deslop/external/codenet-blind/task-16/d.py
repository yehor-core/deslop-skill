from itertools import combinations

def solve(N, K, A):
    MOD = 10**9 + 7
    max_product = float('-inf')
    
    for comb in combinations(A, K):
        product = 1
        for num in comb:
            product *= num
        max_product = max(max_product, product)
    
    return max_product % MOD

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = solve(N, K, A)
    print(result)

if __name__ == '__main__':
    main()
