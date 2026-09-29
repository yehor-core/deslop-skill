import sys
N=int(sys.stdin.readline().strip())
if N%2:
    print(0)
else:
    k=N//2
    ans=0
    while k:
        k//=5
        ans+=k
    print(ans)
