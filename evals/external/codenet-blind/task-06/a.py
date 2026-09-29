from collections import deque
# 木構造を作る
N,M = map(int, input().split())

G = [[] for i in range(3*N)]
for i in range(M):
    # グラフに頂点を追加(距離があるときは,u,vの後に入れる)
    u,v = map(int,input().split())
    G[3*(u-1)].append((3*(v-1)+1))
    G[3*(u-1)+1].append((3*(v-1)+2))
    G[3*(u-1)+2].append((3*(v-1)))

S,T = map(int, input().split())

# 木をBFSをする
used = [-1] * (3*N)
# used[3*(S-1)] = 0 # 始めどこから行くか
q = deque([S-1])
while len(q) > 0:
    a = q.popleft()
    d = used[a]
    Vs = G[a]
    for u in Vs: # 頂点以外の要素がグラフにあるときはここ
        if used[u] == -1:
            q.append(u)
            used[u] = d+1
print(used[3*(T-1)]//3)
