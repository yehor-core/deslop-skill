import sys

def solve():
    N = int(sys.stdin.readline())

    if N % 2 != 0:
        print(0)
        return

    count = 0
    power_of_5 = 5
    while power_of_5 <= N:
        count += N // power_of_5
        if power_of_5 > N // 5: # Prevent overflow
            break
        power_of_5 *= 5
    print(count)

solve()
