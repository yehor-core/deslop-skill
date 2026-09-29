```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(N, K):
    MOD = 10**9 + 7
    
    # Precompute the count of sequences with each GCD
    dp = [0] * (K + 1)
    
    # Iterate through all possible GCD values from 1 to K
    for g in range(1, K + 1):
        # Compute the number of sequences with GCD = g
        count = 0
        for multiple in range(g, K + 1, g):
            count += (K // multiple) ** N
        
        # Subtract the count of sequences with GCD > g
        for h in range(2 * g, K + 1, g):
            count -= dp[h]
        
        dp[g] = count % MOD
    
    # Compute the sum of GCDs
    total_sum = 0
    for g in range(1, K + 1):
        total_sum += g * dp[g]
        total_sum %= MOD
    
    return total_sum

# Read input
N, K = map(int, input().split())

# Solve and print the result
print(solve(N, K))
```
