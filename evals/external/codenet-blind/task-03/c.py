import sys
D,G=map(int,sys.stdin.readline().split())
p=[0]*D
c=[0]*D
for i in range(D):
    pi,ci=map(int,sys.stdin.readline().split())
    p[i]=pi
    c[i]=ci
ans=10**18
for mask in range(1<<D):
    score=0
    cnt=0
    for i in range(D):
        if mask>>i&1:
            score+=p[i]*100*(i+1)+c[i]
            cnt+=p[i]
    if score>=G:
        ans=min(ans,cnt)
        continue
    rem=G-score
    need_cnt=cnt
    for i in range(D-1,-1,-1):
        if mask>>i&1: continue
        val=100*(i+1)
        maxp=p[i]
        req=(rem+val-1)//val
        take=min(req,maxp)
        rem-=take*val
        need_cnt+=take
        if rem<=0:
            ans=min(ans,need_cnt)
            break
print(ans)
