import sys
mod = 10**9+7
input = sys.stdin.readline
N, K = map(int, input().split())
phi = list(range(K+1))
for i in range(2, K+1):
    if phi[i] == i:
        for j in range(i, K+1, i):
            phi[j] -= phi[j] // i
res = 0
for t in range(1, K+1):
    res = (res + phi[t] * pow(K//t, N, mod)) % mod
print(res)
