import sys

def solve():
    N, T = map(int, sys.stdin.readline().split())
    dishes = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        dishes.append((a, b))

    dishes.sort()

    dp = [[0] * (T + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        time_needed, deliciousness = dishes[i-1]
        for j in range(T + 1):
            # Option 1: Don't eat dish i
            dp[i][j] = dp[i-1][j]

            # Option 2: Eat dish i
            # We can order dish i if the time to order it (j) is within T
            # The time to order the dish is the sum of times of previously ordered dishes
            if j >= time_needed:
                # If we order dish i at time j, the previous dishes must have been eaten by time j-time_needed.
                # However, the problem states that you can no longer place an order after T-0.5 minutes.
                # This means that the time taken to eat the *last* dish must be less than or equal to T.
                # The total time spent on eating dishes must be less than or equal to T.
                # If we order dish i, the time at which we finish eating it is the time we started eating it + its eating time.
                # The constraint is that the order must be placed before T - 0.5.
                # This means the sum of `A_i` for all chosen dishes must be <= T.
                # If we choose dish i, it means we have accumulated `time_needed` minutes up to this point
                # and the remaining time available for ordering is `j - time_needed`.
                # The total time spent on previous dishes would be `j - time_needed`.
                # This value `j` here represents the *total time elapsed* when we *finish* eating the i-th dish IF we only consider eating time.
                # The problem implies the total time *spent eating* must be <= T.
                # If the i-th dish is eaten, the total time taken to order and finish it should be considered.
                # The key constraint is about ordering: "After T-0.5 minutes from the first order, you can no longer place a new order".
                # This implies the sum of `A_i` for ordered dishes must be <= T.
                # If we decide to eat dish `i` (which takes `time_needed`), and the total time available for ordering is `j`,
                # then the previous dishes must have taken `j - time_needed` time.
                # The value `j` in `dp[i][j]` is the *total time* spent on eating dishes among the first `i` dishes, if dish `i` is the last one eaten.
                # If we choose dish i, then the total time spent eating is `time_needed` + time spent on previous dishes.
                # The total time spent eating should be <= T.
                # Let's rethink the DP state.
                # dp[i][current_time] = maximum deliciousness using first i dishes, with a total eating time of current_time.
                # This is a standard 0/1 knapsack formulation.
                # If we take dish `i` (cost `time_needed`, value `deliciousness`):
                # We must have had `current_time - time_needed` time available from previous dishes.
                # The condition is `current_time >= time_needed`.

                # Correct interpretation:
                # dp[i][time_spent] = max deliciousness using first i dishes, total eating time is exactly `time_spent`.
                # This is not quite right as we can have any time up to T.
                # Let's use: dp[i][time_spent] = max deliciousness using first i dishes, total eating time is *at most* `time_spent`.

                # If we consider the i-th dish (with time A_{i-1} and deliciousness B_{i-1}):
                # dp[i][j] = max deliciousness using first i dishes, with total eating time at most j.
                # To compute dp[i][j]:
                # 1. Don't eat dish i: dp[i-1][j]
                # 2. Eat dish i: If j >= A_{i-1}, then dp[i-1][j - A_{i-1}] + B_{i-1}

                if j >= time_needed:
                    dp[i][j] = max(dp[i][j], dp[i-1][j - time_needed] + deliciousness)

    # The maximum happiness is the maximum value in the last row of dp, up to time T.
    # Since dp[i][j] already represents "at most j", we just need dp[N][T].
    print(dp[N][T])

solve()
