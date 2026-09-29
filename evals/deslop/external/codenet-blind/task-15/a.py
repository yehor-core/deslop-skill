import sys
import threading
def main():
    import sys
    from math import gcd
    mod = 1000000007
    input = sys.stdin.readline
    N = int(input())
    cnt = {}
    zero = 0
    for _ in range(N):
        a,b = map(int, input().split())
        if a==0 and b==0:
            zero += 1
        else:
            g = gcd(abs(a), abs(b))
            a//=g; b//=g
            if a<0:
                a = -a; b = -b
            elif a==0 and b<0:
                b = -b
            cnt[(a,b)] = cnt.get((a,b), 0) + 1
    maxn = N
    pow2 = [1] * (maxn+1)
    for i in range(1, maxn+1):
        pow2[i] = pow2[i-1] * 2 % mod
    res = 1
    visited = set()
    for key, x in list(cnt.items()):
        if key in visited: continue
        a,b = key
        orth = (b, -a)
        if orth in cnt:
            y = cnt[orth]
        else:
            y = 0
        res = res * (pow2[x] + pow2[y] - 1) % mod
        visited.add(key)
        visited.add(orth)
    ans = (res - 1 + zero) % mod
    print(ans)
if __name__ == "__main__":
    main()
