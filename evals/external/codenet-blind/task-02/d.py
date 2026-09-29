```python
import sys

def solve():
    N, A, B = map(int, sys.stdin.readline().split())
    v = list(map(int, sys.stdin.readline().split()))

    v.sort(reverse=True)

    max_mean = -1.0
    max_ways = 0

    for k in range(A, B + 1):
        current_sum = sum(v[:k])
        current_mean = current_sum / k

        if current_mean > max_mean:
            max_mean = current_mean
            
            # Calculate ways for this k
            if k == 0:
                max_ways = 1
                continue

            # Count occurrences of the k-th largest element
            target_value = v[k - 1]
            
            count_first_k = 0
            for i in range(k):
                if v[i] == target_value:
                    count_first_k += 1

            # Count occurrences of the target value in the entire list
            total_count_target = v.count(target_value)

            # Calculate combinations
            from math import comb
            max_ways = comb(total_count_target, count_first_k)
        elif abs(current_mean - max_mean) < 1e-9:
            # If the mean is the same, add ways
            if k == 0:
                max_ways += 1
                continue

            target_value = v[k - 1]
            
            count_first_k = 0
            for i in range(k):
                if v[i] == target_value:
                    count_first_k += 1

            total_count_target = v.count(target_value)

            from math import comb
            max_ways += comb(total_count_target, count_first_k)

    print(f"{max_mean:.9f}")
    print(max_ways)

if __name__ == "__main__":
    solve()
```
