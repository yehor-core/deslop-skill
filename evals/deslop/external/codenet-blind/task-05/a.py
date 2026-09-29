import sys
def main():
    input=sys.stdin.readline
    N,K=map(int,input().split())
    P_max=(N-1)*(N-2)//2
    if K>P_max:
        print(-1)
        return
    t=P_max-K
    edges=[]
    for i in range(2,N+1):
        edges.append((1,i))
    cnt=0
    for i in range(2,N+1):
        for j in range(i+1,N+1):
            if cnt>=t: break
            edges.append((i,j))
            cnt+=1
        if cnt>=t: break
    print(len(edges))
    for u,v in edges:
        print(u,v)

if __name__=="__main__":
    main()
