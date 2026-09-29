import sys
import threading
def main():
    import math
    A,B=map(int,sys.stdin.read().split())
    g=math.gcd(A,B)
    n=g
    cnt=0
    if n%2==0:
        cnt+=1
        while n%2==0:
            n//=2
    p=3
    while p*p<=n:
        if n%p==0:
            cnt+=1
            while n%p==0:
                n//=p
        p+=2
    if n>1:
        cnt+=1
    print(cnt+1)
if __name__=='__main__':
    main()
