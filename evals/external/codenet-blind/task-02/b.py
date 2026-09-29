import bisect
import math
from scipy.misc import comb

N,A,B=map(int,input().split())
List=list(map(int,input().split()))
List = sorted(List, reverse=True)

mini = List[A-1]
ans = 0

if List[A-1] != List[A]:
  ans = sum(List[:A])/A
  print(ans)
  print(1)

else:
  num = List.count(List[A-1])
  List = sorted(List)
  num2 = N - bisect.bisect_right(List,List[A-1])
  List = sorted(List, reverse=True)
  
  if List[0] != List[A-1]:
    B = A
  for i in range(B-A+1):
    n = num
    kosuu = A + i - num2
    ans  = int(ans + math.factorial(n) // (math.factorial(n - kosuu) * math.factorial(kosuu)))
  
  ave = int(sum(List[:A])/A)
  print(ave)
  print(ans)
