#https://atcoder.jp/contests/abc104/tasks/abc104_c

d, g = map(int, input().split())

for i in range(d):
  pc.append(list(map(int,input().split())))

ans = float("inf")

#各配点について解くか解かないかを決め、その上で G 点に満たなければ、まだ解いてない配点のうち一番高い配点のものを足りない分解く

for i in range(2**d):
    count = 0 #解く問題数
    sum = 0
    nokori = set(range(1, d + 1)) #点数の列

    for j in range(d):
        if (i>>j)&1:
            sum += pc[j][0] * (j + 1) * 100 + pc[j][1] #(j+1)*100点+bounus
            count += pc[j][0]
            nokori.discard(j + 1) #(j+1)*100点を処理したので削除

    # G 点に満たなければ nokori のうち一番大きいものを解く
    if sum < g:
        use = max(nokori)
        # 解く問題が問題数を超えないように注意
        n = min(pc[use - 1][0], -(-(g - sum) // (use * 100)))
        count += n
        sum += n * use * 100

    if sum >= g:
        #数が小さい方を残す
        ans = min(ans, count)

print(ans)
