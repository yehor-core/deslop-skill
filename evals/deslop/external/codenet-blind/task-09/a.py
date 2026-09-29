```python
def solve(N, T, A, B):
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(T + 1):
            # Don't order this dish
            dp[i][j] = dp[i-1][j]
            
            # Order this dish if possible
            if j >= A[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j - A[i-1]] + B[i-1])
    
    return max(dp[N])

def main():
    N, T = map(int, input().split())
    A = []
    B = []
    
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    print(solve(N, T, A, B))

if __name__ == "__main__":
    main()
```
