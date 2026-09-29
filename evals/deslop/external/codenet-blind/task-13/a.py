n=int(input())
A=[]
B=[]
c=0
for i in range(n):
  S=input()
  a=0
  b=0
  for j in range(len(S)):
    if S[j]=="(":
      a=a+1
    else:
      a=a-1
      if a<b:
        b=a
  if b==0:
    c=c+a
  elif a>0:
    B.append[(b,-1*a)]
  else:
    A.append([-1*b,a])
A.sort()
B.sort()
f=0
for i in range(len(B)):
  if c+B[i][0]<0:
    f=1
  c=c-A[i][1]
for i in range(len(A)):
  if c-A[i][0]<0:
    f=1
  c=c+A[i][1]
if c!=0:
  f=1
if f==0:
  print("Yes")
else:
  print("No")
