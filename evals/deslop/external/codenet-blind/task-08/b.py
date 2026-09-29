import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_prime_factors(n):
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors

def solve():
    a, b = map(int, input().split())
    g = gcd(a, b)

    if g == 1:
        print(1)
        return

    prime_factors = get_prime_factors(g)

    count = 1
    for p in prime_factors:
        if g % p == 0:
            count += 1
            while g % p == 0:
                g //= p
        if g == 1:
            break

    if g > 1:
        count += 1

    print(count)

solve()
