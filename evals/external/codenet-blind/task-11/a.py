import sys

def solve():
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort(reverse=True)

    possible_handshakes = []
    for i in range(N):
        for j in range(N):
            possible_handshakes.append((A[i] + A[j], i, j))

    possible_handshakes.sort(key=lambda x: x[0], reverse=True)

    total_happiness = 0
    used_pairs = set()
    count = 0

    for happiness, i, j in possible_handshakes:
        if count == M:
            break

        # The problem states that (x, y) cannot be repeated.
        # If we represent guests by their indices after sorting,
        # we need to consider that guest with index `i` and guest with index `j`
        # can be distinct even if A[i] == A[j].
        # However, the sample case interpretation seems to suggest that
        # the pair of *powers* (A_x, A_y) can be considered, but
        # the constraint is about the specific guests.
        # The problem says "chooses one (ordinary) guest x ... and another guest y".
        # This implies we are choosing guests by their original identity, not just their power.
        # However, since we only have powers and N is large, we can't track original identities.
        # The sorting implies we are picking based on power.
        # The crucial part is "there is no pair p, q (1 <= p < q <= M) such that (x_p, y_p) = (x_q, y_q)".
        # This means if we pick guest 4 (power 34) and guest 5 (power 33) in one handshake,
        # we cannot pick guest 4 and guest 5 again in that exact order.
        # We can pick guest 5 and guest 4.

        # Let's re-evaluate the interpretation based on the sample:
        # Sample 1: 5 3, powers: 10 14 19 34 33
        # Sorted powers: 34, 33, 19, 14, 10
        # Handshake 1: Guest 4 (34) left, Guest 4 (34) right. Happiness: 34+34 = 68. Pair (4, 4)
        # Handshake 2: Guest 4 (34) left, Guest 5 (33) right. Happiness: 34+33 = 67. Pair (4, 5)
        # Handshake 3: Guest 5 (33) left, Guest 4 (34) right. Happiness: 33+34 = 67. Pair (5, 4)
        # Total = 68 + 67 + 67 = 202.

        # This means the indices `i` and `j` in `possible_handshakes` refer to the indices
        # in the *sorted* list `A`.
        # So `A[i]` is the power of one guest and `A[j]` is the power of another guest.
        # The constraint is on the *pair of indices* in the sorted list.
        # If we select `A[i]` for the left hand and `A[j]` for the right hand,
        # we cannot select the same pair `(i, j)` again.
        # We can select `(i, j)` and `(j, i)` as distinct handshakes if i != j.

        if (i, j) not in used_pairs:
            total_happiness += happiness
            used_pairs.add((i, j))
            count += 1

    print(total_happiness)

solve()
```
