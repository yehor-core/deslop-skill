N=int(input())

if N%2==1:
    print(0)
else:
    ans=0
    div=10
    while N//div>0:
        ans+=N//div
        div*=5
print(ans)
