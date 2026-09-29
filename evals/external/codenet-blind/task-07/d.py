import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
mod=10**9+7
N,K=map(int,input().split())
adj=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
ans=K%mod
stack=[(1,0)]
while stack:
    u,p=stack.pop()
    avail=K-1 if p==0 else K-2
    cnt=0
    for v in adj[u]:
        if v==p: continue
        ans=ans*(avail-cnt)%mod
        cnt+=1
        stack.append((v,u))
print(ans)
