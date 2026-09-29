n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

mia = sorted([i for i in a if i < 0], reverse=True)
pla = sorted([i for i in a if i >= 0])
ans, num = 1, []

if len(pla) == 0 and k % 2 == 1:
    for i in mia[:k]:
        ans = ans * i % mod
    print(ans)
    exit()

for _ in range(k):
    if len(mia) > 0 and len(pla) > 0:
        if abs(mia[-1]) < pla[-1]:
            tmp = pla.pop()
        elif abs(mia[-1]) >= pla[-1]:
            tmp = mia.pop()
    elif len(mia) == 0:
        tmp = pla.pop()
    elif len(pla) == 0:
        tmp = mia.pop()
    num.append(tmp)

cnt = sum(i < 0 for i in num)
for i in num:
    ans = ans * i % mod

if cnt % 2 == 1:
    if len(mia) > 0 and cnt != k:
        for i in num[::-1]:
            if i >= 0:
                p, q = i, mia[-1]
                break
        if len(pla) == 0:
            ans *= q * pow(p, mod - 2, mod)
    if len(pla) > 0:
        for i in num[::-1]:
            if i < 0:
                r, s = i, pla[-1]
                break
        if len(mia) == 0 or cnt == k:
            ans *= s * pow(r, mod - 2, mod)
    if len(mia) > 0 and len(pla) > 0 and cnt != k:
        if p * r >= q * s:
            ans *= s * pow(r, mod - 2, mod)
        if p * r < q * s:
            ans *= q * pow(p, mod - 2, mod)
    ans %= mod
print(ans)
