s = input().split()
A=int(s[0])
B=int(s[1])

def factorization(n):
    p=[]
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            p.append(i)

    if temp!=1:
        arr.append([temp, 1])
        p.append(temp)

    if arr==[]:
        arr.append([n, 1])
        p.append(n)

    return p
A_fact=[]
B_fact=[]
answer=[]
count=0

A_fact=factorization(A)
B_fact=factorization(B)

for p in A_fact:
    if p in B_fact:
            answer.append(p)
            count+=1
if A==1 and B==1:
    print(count)
else:
    print(count+1)
