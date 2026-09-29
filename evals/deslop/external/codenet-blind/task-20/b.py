import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))

a = max(A)
b = min(A)
A.pop(a)
A.pop(b)

ans = a-b
for i in range(n-2):
    ans += abs(A[i])
print(ans)

for i in range(n-2):
    if A[i] > 0:
        print(b, A[i])
        b -= A[i]
    else:
        print(a, A[i])
        a -= A[i]
print(a, b)
