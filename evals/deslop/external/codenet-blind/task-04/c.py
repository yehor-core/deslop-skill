s = input()
MOD = 10 ** 9 + 7
n = len(s)
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)
dp1[0] = 1
for i in range(n):
    if s[i] == '1':
        dp1[i + 1] += dp1[i] * 2
        dp1[i + 1] %= MOD
        dp2[i + 1] += dp1[i] + dp2[i] * 3
        dp2[i + 1] %= MOD
    else:
        dp1[i + 1] += dp1[i]
        dp1[i + 1] %= MOD
        dp2[i + 1] += dp2[i] * 3
        dp2[i + 1] %= MOD

print((dp1[n] + dp2[n]) % MOD)
