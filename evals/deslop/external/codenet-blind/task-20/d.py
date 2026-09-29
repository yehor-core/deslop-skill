```python
import sys

def solve():
    N = int(sys.stdin.readline())
    A = [int(sys.stdin.readline()) for _ in range(N)]

    A.sort()

    positive_part = A[1:]
    negative_part = A[:-1]

    if all(x >= 0 for x in A):
        max_val = sum(A[1:]) - A[0]
        operations = []
        current_val = A[0]
        for val in A[1:]:
            operations.append((current_val, val))
            current_val -= val
        operations.append((current_val, 0))
        print(max_val)
        for x, y in operations:
            print(x, y)
        return

    if all(x <= 0 for x in A):
        max_val = A[-1] - sum(A[:-1])
        operations = []
        current_val = A[-1]
        for val in reversed(A[:-1]):
            operations.append((current_val, val))
            current_val -= val
        operations.append((current_val, 0))
        print(max_val)
        for x, y in operations:
            print(x, y)
        return

    positive_sum = sum(x for x in A if x >= 0)
    negative_sum = sum(x for x in A if x < 0)

    max_val = positive_sum - negative_sum
    operations = []

    current_pos_sum = 0
    for val in A:
        if val >= 0:
            if current_pos_sum == 0:
                current_pos_sum = val
            else:
                operations.append((current_pos_sum, val))
                current_pos_sum -= val

    current_neg_sum = 0
    for val in reversed(A):
        if val < 0:
            if current_neg_sum == 0:
                current_neg_sum = val
            else:
                operations.append((val, current_neg_sum))
                current_neg_sum -= val

    if current_pos_sum != 0:
        operations.append((current_pos_sum, current_neg_sum))
    else:
        operations.append((current_neg_sum, current_pos_sum))


    print(max_val)
    for x, y in operations:
        print(x, y)


solve()
```
