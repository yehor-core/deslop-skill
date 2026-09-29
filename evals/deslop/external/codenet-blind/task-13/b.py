import sys

def solve():
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().strip() for _ in range(N)]

    open_needed = 0
    close_needed = 0
    balance_diff = 0
    min_balance = 0

    for s in S:
        current_balance = 0
        for char in s:
            if char == '(':
                current_balance += 1
            else:
                current_balance -= 1
            min_balance = min(min_balance, current_balance)

        if min_balance < 0:
            if current_balance < 0:
                close_needed += abs(current_balance)
            else:
                open_needed += abs(min_balance)
        else:
            open_needed += min_balance
        min_balance = 0

    if open_needed == 0 and close_needed == 0:
        print("Yes")
    else:
        print("No")

solve()
