import sys

MOD = 10**9 + 7

def solve():
    N, K = map(int, sys.stdin.readline().split())

    # dp[g] will store the number of sequences (A_1, ..., A_N) such that gcd(A_1, ..., A_N) is a multiple of g.
    # Since we need to compute the sum of gcds, we can use the principle of inclusion-exclusion.
    # However, a more direct approach is to sum up g * (number of sequences where gcd is exactly g).
    # Let f(g) be the number of sequences where gcd(A_1, ..., A_N) = g.
    # The sum we want is sum_{g=1 to K} g * f(g).
    #
    # Let F(g) be the number of sequences where gcd(A_1, ..., A_N) is a multiple of g.
    # If gcd(A_1, ..., A_N) is a multiple of g, then each A_i must be a multiple of g.
    # The multiples of g between 1 and K are g, 2g, 3g, ..., floor(K/g) * g.
    # There are floor(K/g) such multiples.
    # So, for each A_i, there are floor(K/g) choices.
    # Thus, F(g) = (floor(K/g))^N.
    #
    # We know that F(g) = sum_{m=1 to floor(K/g)} f(m*g).
    # Using Mobius inversion, f(g) = sum_{m=1 to floor(K/g)} mu(m) * F(m*g).
    # The sum we want is sum_{g=1 to K} g * f(g)
    # = sum_{g=1 to K} g * (sum_{m=1 to floor(K/g)} mu(m) * F(m*g))
    # Let j = m*g. Then m = j/g.
    # = sum_{g=1 to K} g * (sum_{j=g, g|j to K} mu(j/g) * F(j))
    # Swap the order of summation:
    # = sum_{j=1 to K} F(j) * (sum_{g=1, g|j to K} g * mu(j/g))
    #
    # Let's rephrase the problem using the property that sum_{d|n} phi(d) = n.
    # We want to compute sum_{A_1, ..., A_N} gcd(A_1, ..., A_N).
    # sum_{A_1, ..., A_N} gcd(A_1, ..., A_N) = sum_{A_1, ..., A_N} sum_{g | gcd(A_1, ..., A_N)} phi(g)
    # Swap the order of summation:
    # = sum_{g=1 to K} phi(g) * (number of sequences where g | gcd(A_1, ..., A_N))
    # The condition g | gcd(A_1, ..., A_N) means that g divides every A_i.
    # So, each A_i must be a multiple of g.
    # The multiples of g in the range [1, K] are g, 2g, ..., floor(K/g) * g.
    # There are floor(K/g) such multiples.
    # So, for each A_i, there are floor(K/g) choices.
    # The number of such sequences is (floor(K/g))^N.
    #
    # Therefore, the answer is sum_{g=1 to K} phi(g) * (floor(K/g))^N mod (10^9+7).

    # Precompute Euler's totient function (phi) up to K
    phi = list(range(K + 1))
    for i in range(2, K + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, K + 1, i):
                phi[j] -= phi[j] // i

    total_sum = 0
    for g in range(1, K + 1):
        num_multiples = K // g
        # Calculate (num_multiples)^N mod MOD efficiently
        count = pow(num_multiples, N, MOD)
        term = (phi[g] * count) % MOD
        total_sum = (total_sum + term) % MOD

    print(total_sum)

solve()
