from typing import List

def solve() -> None:
    L_str = input()
    n = len(L_str)
    MOD = 10**9 + 7

    # The condition a + b = a XOR b is equivalent to saying that there are no carries
    # when adding a and b in binary. This means that for every bit position k,
    # it's not possible for both a and b to have a 1 at that position.
    # In other words, if the k-th bit of a is b_k_a and the k-th bit of b is b_k_b,
    # then we cannot have b_k_a = 1 and b_k_b = 1 simultaneously.
    # This implies that for each bit position, the pair of bits (b_k_a, b_k_b) can be
    # (0, 0), (0, 1), or (1, 0).

    # We are looking for pairs (a, b) such that a + b <= L and a + b = a XOR b.
    # The second condition means that for every bit position k, if the k-th bit of a is a_k
    # and the k-th bit of b is b_k, then a_k AND b_k must be 0.
    # This is equivalent to saying that a_k + b_k is either 0 or 1 for all k.
    #
    # So, for each bit position i (from most significant to least significant):
    # If L_i is 0:
    #   Then a_i and b_i must both be 0. (Because if either were 1, then a+b would be at least 2^i, which would be > L if L only has 0s at higher bits)
    # If L_i is 1:
    #   We have three choices for (a_i, b_i): (0, 0), (0, 1), (1, 0).
    #   If we choose (0, 0), then the sum up to this bit is 0. The remaining bits of a and b can be anything such that their sum is <= the remaining part of L.
    #   If we choose (0, 1) or (1, 0), then the sum up to this bit is 1. The remaining bits of a and b can be anything such that their sum is <= the remaining part of L shifted by one bit to the right (effectively subtracting 1 from L).

    # Let dp[i][0] be the number of pairs (a, b) such that:
    # 1. The bits of a and b from position n-1 down to i are determined.
    # 2. The sum of these determined bits is strictly less than the first i bits of L.
    # 3. For all determined bit positions, the k-th bit of a AND the k-th bit of b is 0.
    #
    # Let dp[i][1] be the number of pairs (a, b) such that:
    # 1. The bits of a and b from position n-1 down to i are determined.
    # 2. The sum of these determined bits is exactly equal to the first i bits of L.
    # 3. For all determined bit positions, the k-th bit of a AND the k-th bit of b is 0.

    # We iterate from the most significant bit (MSB) to the least significant bit (LSB).
    # Let's use 0-based indexing for bits, from MSB (index 0) to LSB (index n-1).
    # dp[i][0]: number of ways to assign bits from i to n-1 such that the sum
    #           is strictly less than L[i:]
    # dp[i][1]: number of ways to assign bits from i to n-1 such that the sum
    #           is exactly equal to L[i:]

    # Base case: After considering all bits (i.e., beyond the LSB)
    # dp[n][0] = 1 (the empty prefix sums to 0, which is < anything)
    # dp[n][1] = 0 (the empty prefix cannot sum to a non-zero value)

    # Let's rephrase the DP state to be more intuitive for processing from MSB.
    # dp[i][tight]: number of pairs (a, b) considering bits from MSB up to bit i-1,
    #               where 'tight' is a boolean.
    #               'tight' is True if the sum formed by a and b so far matches the prefix of L.
    #               'tight' is False if the sum formed by a and b so far is strictly less than the prefix of L.
    #
    # dp[i][0]: Number of ways to fill bits from 0 to i-1 such that the sum of (a_k XOR b_k) for k from 0 to i-1
    #           is strictly less than the prefix L[0...i-1]. This means there was a 'tight' break at some earlier bit.
    # dp[i][1]: Number of ways to fill bits from 0 to i-1 such that the sum of (a_k XOR b_k) for k from 0 to i-1
    #           is exactly equal to the prefix L[0...i-1]. This means all prior bits matched L exactly.

    # dp[i][tight_flag] where i is the current bit position we are considering (from 0 to n)
    # tight_flag = 0: current sum is strictly less than prefix of L
    # tight_flag = 1: current sum is exactly equal to prefix of L

    # dp[0][1] = 1 (empty prefix, sum is 0, which is equal to L's empty prefix)
    # dp[0][0] = 0

    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][1] = 1

    for i in range(n): # Iterate through bit positions from MSB to LSB
        l_bit = int(L_str[i])

        # Transitions for dp[i+1][0] (current sum < L's prefix)
        # To reach dp[i+1][0] (sum < L's prefix):
        # Case 1: From dp[i][0] (previous sum < L's prefix)
        #   Regardless of L[i], we can choose (a_i, b_i) to be (0,0), (0,1), or (1,0).
        #   The sum at bit i will be a_i ^ b_i.
        #   Since the previous sum was already less than L's prefix, this new sum will also be less than L's prefix.
        #   So, from dp[i][0], we can transition to dp[i+1][0] in 3 ways:
        #   (0,0) -> sum_bit = 0
        #   (0,1) -> sum_bit = 1
        #   (1,0) -> sum_bit = 1
        dp[i+1][0] = (dp[i+1][0] + dp[i][0] * 3) % MOD

        # Case 2: From dp[i][1] (previous sum == L's prefix)
        #   We need to make the current sum < L's prefix.
        #   If L[i] is 1:
        #     We can choose (a_i, b_i) as (0,0) -> sum_bit = 0. This is < L[i]=1. Transition to dp[i+1][0].
        #     We can choose (a_i, b_i) as (0,1) -> sum_bit = 1. This == L[i]=1. Transition to dp[i+1][1].
        #     We can choose (a_i, b_i) as (1,0) -> sum_bit = 1. This == L[i]=1. Transition to dp[i+1][1].
        #   If L[i] is 0:
        #     We can only choose (a_i, b_i) as (0,0) -> sum_bit = 0. This == L[i]=0. Transition to dp[i+1][1].
        #     We cannot choose (0,1) or (1,0) because that would make sum_bit=1, which is > L[i]=0.

        if l_bit == 1:
            # From dp[i][1], if we choose (a_i, b_i) = (0,0), sum_bit = 0. This is < L[i]=1.
            # Transition to dp[i+1][0].
            dp[i+1][0] = (dp[i+1][0] + dp[i][1] * 1) % MOD

            # From dp[i][1], if we choose (a_i, b_i) = (0,1) or (1,0), sum_bit = 1. This is == L[i]=1.
            # Transition to dp[i+1][1].
            dp[i+1][1] = (dp[i+1][1] + dp[i][1] * 2) % MOD
        else: # l_bit == 0
            # From dp[i][1], if we choose (a_i, b_i) = (0,0), sum_bit = 0. This is == L[i]=0.
            # Transition to dp[i+1][1].
            dp[i+1][1] = (dp[i+1][1] + dp[i][1] * 1) % MOD
            # We cannot choose (0,1) or (1,0) from dp[i][1] when L[i]=0, because that would make sum > L[i].

    # The final answer is the sum of counts where the total sum is <= L.
    # This corresponds to cases where the final sum is strictly less than L (dp[n][0])
    # or exactly equal to L (dp[n][1]).
    print((dp[n][0] + dp[n][1]) % MOD)

solve()
