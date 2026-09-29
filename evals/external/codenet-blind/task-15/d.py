MOD = 10**9 + 7
import sys
from collections import defaultdict
input = sys.stdin.readline
N= int(input())
AB = [list(map(int,input().split())) for i in range(N)]

def gcd(a,b):
    while a:
        b,a = a, b%a
    return b

ans = 0

PAB = []
for a,b in AB:
    d = gcd(a,b)
    if d == 0:
        PAB.append((0,0))
        continue
    PAB.append((a//d,b//d)) # a//d >= 0
    
dic1 = defaultdict(int)
dic4 = defaultdict(int)

yaxis = 0
xaxis = 0
origin = 0
vs = []
for a,b in PAB:
    if a == 0 and b == 0:
        origin += 1
        continue
    if a == 0:
        yaxis += 1
        continue
    if b == 0:
        xaxis += 1
        continue
    if b > 0:
        dic1[(a,b)] += 1
        vs.append((a,b))
    else:
        dic4[(-b,a)] += 1
        vs.append((-b,a))

vs = list(set(vs))

ans = 1
for v in vs:
    n1 = dic1[v]
    n4 = dic4[v]
    ans *= (pow(2,n1,MOD) + pow(2,n4,MOD) - 1)
    ans %= MOD

ans *= (pow(2,xaxis,MOD)+pow(2,yaxis,MOD)-1)
ans -= 1 # no fish
ans += origin
print(ans % MOD)
