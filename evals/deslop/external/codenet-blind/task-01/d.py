H,W=map(int,input().split())
S=[]
for _ in range(H):
    S.append(input())

def path(i,j):
    p=[]
    for k in [1,-1]:
        if 0<=i+k<H:
            if S[i][j]!=S[i+k][j]:
                p.append((i+k,j))
        if 0<=j+k<W:
            if S[i][j]!=S[i][j+k]:
                p.append((i,j+k))
    return p
f = [[0 for i in range(W)] for j in range(H)]
ans=0

for i in range(H):
    for j in range(W):
        if f[i][j]==0:
            f[i][j]=1
            b=0
            w=0
            if S[i][j]=='#':
                b+=1
            else:
                w+=1
            que=path(i,j)

            while len(que)>0:
                tmp=[]
                for q in que:
                    q0,q1=q
                    if f[q0][q1]==0:
                        f[q0][q1]=1
                        if S[q0][q1]=='#':
                            b+=1
                        else:
                            w+=1
                        for p in path(q0,q1):
                            if f[p[0]][p[1]]==0:
                                tmp.append(p)
                que=tmp
            ans+=b*w
print(ans)
