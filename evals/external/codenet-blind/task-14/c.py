n, m, x = map(int, input().split())
C = {}
ans = 0
sums = [0] * m
for _ in range(n):
    c = [int(x) for x in input().split()]
    C[c[0]] = c[1:]
    ans += c[0]
    for i in range(m):
        sums[i] += c[i + 1]
if min(sums) < x:
    print(-1)
    exit()
C = sorted(C.items(), reverse=True)
for c, A in C:
    sums_ = list(sums)
    minused = True
    for i, a in enumerate(A):
        sums_[i] -= a
        if sums_[i] < x:
            minused = False
            break
    if minused:
        sums = sums_
        ans -= c
print(ans)
