import sys

input = sys.stdin.readline
mod = 10**9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
P = []
N = []
for a in A:
  if a >= 0:
    P.append(a)
  else:
    N.append(a)
N.reverse()
P.sort(reverse=True)
N.sort(reverse=True)
ans = -10**18
if K % 2 == 1:
  ans = P[0]
  P = P[1:]
  K -= 1
if K == 0:
  print(ans % mod)
  exit()
P_cnt = len(P)
N_cnt = len(N)
l = 0
r = 0
while K > 0:
  if l + 1 < P_cnt and r + 1 < N_cnt:
    p_prod = P[l] * P[l + 1]
    n_prod = N[r] * N[r + 1]
    if p_prod >= n_prod:
      ans *= p_prod
      ans %= mod
      l += 2
      K -= 2
    else:
      ans *= n_prod
      ans %= mod
      r += 2
      K -= 2
  elif l + 1 < P_cnt:
    ans *= P[l] * P[l + 1]
    ans %= mod
    l += 2
    K -= 2
  elif r + 1 < N_cnt:
    ans *= N[r] * N[r + 1]
    ans %= mod
    r += 2
    K -= 2
  else:
    break
print(ans % mod)
