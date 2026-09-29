import sys
readline = sys.stdin.readline
write = sys.stdout.write
flush = sys.stdout.flush

# クエリ: "? x1 x2" を出力
def query(x1):
    write("? %d\n" % (x1))
    flush()
    # ジャッジから返される値を取得
    return readline()

n = int(input())
l = 0
r = n-1
mid = r // 2
re = [None] * n
re[0] = query(0)
if re[0] == "Vacant":
  exit()
re[mid] = query(mid)
while re[mid] != "Vacant":
  if re[l] == re[mid]:
    if (mid - l) % 2:
      r = mid
    else:
      l = mid
  else:
    if (mid - l) % 2:
      l = mid
    else:
      r = mid
  mid = (l + r) // 2
  re[mid] = query(mid)
exit()
