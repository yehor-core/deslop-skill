```python
def solve(N):
    if N < 2:
        return 0
    
    # Count number of pairs of 2 and 5 as prime factors
    twos = 0
    fives = 0
    
    for i in range(2, N+1, 2):
        curr = i
        while curr % 2 == 0:
            twos += 1
            curr //= 2
        
        while curr % 5 == 0:
            fives += 1
            curr //= 5
    
    # Return the minimum of number of 2s and 5s
    return min(twos, fives)

# Read input and solve
N = int(input())
print(solve(N))
```
