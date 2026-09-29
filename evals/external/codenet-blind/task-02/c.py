import sys,math
data=sys.stdin.read().split()
it=iter(data)
N=int(next(it));A=int(next(it));B=int(next(it))
v=[int(next(it)) for _ in range(N)]
v.sort(reverse=True)
ps=[0]*N
ps[0]=v[0]
for i in range(1,N):ps[i]=ps[i-1]+v[i]
best_num=ps[A-1];best_den=A
for k in range(A,B+1):
    num=ps[k-1];den=k
    if num*best_den>best_num*den:
        best_num=num;best_den=den
total=0
for k in range(A,B+1):
    num=ps[k-1];den=k
    if num*best_den==best_num*den:
        x=v[k-1]
        c=v.count(x)
        a=v[:k].count(x)
        total+=math.comb(c,a)
print("{:.6f}".format(best_num/best_den))
print(total)
