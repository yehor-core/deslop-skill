import sys
N,M=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
A.sort()
P=[0]*(N+1)
for i in range(N):
    P[i+1]=P[i]+A[i]
def count_and_sum(x):
    total_cnt=0
    total_sum=0
    j=N-1
    for i in range(N):
        while j>=0 and A[i]+A[j]>=x:
            j-=1
        pos=j+1
        cnt=N-pos
        total_cnt+=cnt
        total_sum+=cnt*A[i]+(P[N]-P[pos])
    return total_cnt,total_sum
low=2
high=2*A[-1]+1
while low<high:
    mid=(low+high+1)//2
    c,_=count_and_sum(mid)
    if c>=M:
        low=mid
    else:
        high=mid-1
x0=low
cnt_gt,sum_gt=count_and_sum(x0+1)
rem=M-cnt_gt
ans=sum_gt+rem*x0
print(ans)
