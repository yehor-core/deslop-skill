n,m=map(int,input().split())
d=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    d[a]=(d[a]+1)%2
    d[b]=(d[b]+1)%2
print("NO" if any(d) else "YES")
