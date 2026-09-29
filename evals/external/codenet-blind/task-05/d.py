import sys

def solve():
    N, K = map(int, sys.stdin.readline().split())

    if K == 0:
        if N == 2:
            print(1)
            print("1 2")
        else:
            print(N - 1)
            for i in range(1, N):
                print(f"{i} {i+1}")
        return

    edges = []
    dist_2_count = 0

    # Strategy: Create a star graph first, then add edges to reduce distance 2 pairs.
    # The center of the star graph will be vertex 1.
    # Vertices 2 to N will be connected to vertex 1.
    # This gives N-1 edges.
    # For any pair (i, j) where i, j > 1, their distance is 2 if they are not directly connected.
    # The number of such pairs is (N-1) * (N-2) / 2.
    # If K is greater than this, we cannot achieve it with just a star graph.

    max_dist_2_star = (N - 1) * (N - 2) // 2
    if K > max_dist_2_star:
        print("-1")
        return

    # Start with a star graph centered at vertex 1
    for i in range(2, N + 1):
        edges.append((1, i))

    current_dist_2 = max_dist_2_star

    # If K is less than max_dist_2_star, we need to reduce the number of distance 2 pairs.
    # We do this by adding edges between non-center vertices.
    # Adding an edge between two vertices i and j (where i, j > 1)
    # reduces the number of distance 2 pairs by 2.
    # Why 2?
    # Before adding (i, j):
    #   - (i, j) was distance 2 (via 1: i-1-j)
    #   - For any k != 1, i, j: (i, k) was distance 2 if (i, k) is not an edge.
    #                                   (j, k) was distance 2 if (j, k) is not an edge.
    # If we add (i, j):
    #   - (i, j) becomes distance 1. The previous distance 2 path i-1-j is now redundant for shortest distance.
    #   - For any k != 1, i, j:
    #       - If k was distance 2 from i (i-x-k), and x is not 1, then i-x-k is still distance 2.
    #       - If k was distance 2 from j (j-y-k), and y is not 1, then j-y-k is still distance 2.
    #
    # Let's re-evaluate the effect of adding an edge (u, v) where u, v != 1.
    # Initially, all pairs (i, j) where i, j in {2, ..., N} and i != j have distance 2 (path i-1-j).
    # Number of such pairs: (N-1) choose 2 = (N-1)(N-2)/2.
    #
    # Consider adding an edge between vertex `a` and vertex `b`, where `a, b` are in {2, ..., N} and `a != b`.
    # The pair (a, b) was distance 2 (a-1-b). After adding edge (a, b), their distance becomes 1.
    # This reduces the count of distance 2 pairs by 1.
    #
    # What about other pairs?
    # Consider a vertex `c` where `c` is in {2, ..., N} and `c != a`, `c != b`.
    # The pair (a, c) had distance 2 (a-1-c). After adding edge (a, b), it's still distance 2 (a-1-c).
    # BUT, we now have a new path a-b-c. If this is shorter than a-1-c, then the distance (a, c) decreases.
    #
    # Let's reconsider the definition of distance 2.
    # A pair (i, j) has shortest distance 2 if there exists a vertex `v` such that (i, v) is an edge and (v, j) is an edge,
    # and i, j are not directly connected.
    #
    # In a star graph with center 1:
    # - Pairs (1, i) for i > 1 have distance 1.
    # - Pairs (i, j) for i, j > 1, i != j have distance 2 (path i-1-j).
    #   Number of such pairs = (N-1) choose 2.
    #
    # If we add an edge (a, b) where a, b > 1, a != b:
    # 1. Pair (a, b): Distance changes from 2 to 1. Count decreases by 1.
    # 2. For any vertex `c` (c > 1, c != a, c != b):
    #    Pair (a, c): Distance was 2 (a-1-c). Now we have path a-b-c.
    #    If shortest distance between (a, c) was 2, it means a-1-c was the shortest.
    #    Now we have a-b-c. If `b` is adjacent to `c` (which it is, since it's a star graph), then
    #    the distance a-b-c is 2.
    #    So the shortest distance between `a` and `c` is still 2.
    #    This means adding edge (a, b) does NOT change the distance 2 count for pairs like (a, c).
    #
    # This implies adding an edge between two nodes (other than the center) reduces the distance 2 count by EXACTLY 1.
    # The pair (a, b) itself changes from distance 2 to distance 1.
    #
    # So, to reduce the distance 2 count from `max_dist_2_star` to `K`, we need to add `max_dist_2_star - K` edges.
    # These edges should be between vertices in {2, ..., N}.
    # We can pick any `max_dist_2_star - K` distinct pairs from {2, ..., N}.

    edges_to_add_count = max_dist_2_star - K

    if edges_to_add_count > 0:
        added_count = 0
        for i in range(2, N + 1):
            for j in range(i + 1, N + 1):
                if added_count < edges_to_add_count:
                    edges.append((i, j))
                    added_count += 1
                else:
                    break
            if added_count == edges_to_add_count:
                break

    print(len(edges))
    for u, v in edges:
        print(f"{u} {v}")

solve()
