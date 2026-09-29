```python
def solve(N, M, A):
    max_happiness = 0
    used_handshakes = set()

    # Try all possible handshake combinations
    for _ in range(M):
        best_happiness = 0
        best_x = -1
        best_y = -1

        for x in range(N):
            for y in range(N):
                # Check if this handshake has not been used before
                if (x, y) not in used_handshakes:
                    handshake_happiness = A[x] + A[y]
                    if handshake_happiness > best_happiness:
                        best_happiness = handshake_happiness
                        best_x = x
                        best_y = y

        # If no new handshake possible, break
        if best_x == -1:
            break

        # Add handshake and update total happiness
        max_happiness += best_happiness
        used_handshakes.add((best_x, best_y))

    return max_happiness

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))

# Print result
print(solve(N, M, A))
```
