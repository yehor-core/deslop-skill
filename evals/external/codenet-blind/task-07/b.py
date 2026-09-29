from sys import setrecursionlimit
setrecursionlimit(10**6)
n,k=map(int,input().split())
paths=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    paths[a-1].append(b-1)
    paths[b-1].append(a-1)
nums=[-1]*n
nums[0]=k
from collections import deque
now=deque()
now.append(0)
def bfs(d):
    global n,k,paths,nums,now
    l=len(now)
    if d==1:
        for i in range(l):
            p=now.popleft()
            ln=len(paths[p])
            for j in range(ln):
                if nums[paths[p][j]]==-1:
                    nums[paths[p][j]]=k-1-j
                    now.append(paths[p][j])
    else:
        for i in range(l):
            p=now.popleft()
            ln=len(paths[p])
            for j in range(ln):
                if nums[paths[p][j]]==-1:
                    nums[paths[p][j]]=k-2-(j-1)
                    now.append(paths[p][j])
    if len(now):bfs(d+1)
bfs(1)
ans=1
#print(nums)
for i in range(n):
    if nums[i]<=0:
        print(0)
        exit()
    ans*=nums[i]
    ans%=(10**9+7)
print(ans)
