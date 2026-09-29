import sys
input=sys.stdin.readline
N=int(input())
def ask(i):
    print(i)
    sys.stdout.flush()
    s=input().strip()
    if s=="Vacant":
        sys.exit(0)
    return 1 if s=="Female" else 0
half=N//2
a0=ask(0)
ah=ask(half)
if a0==ah:
    l=0; r=half; al=a0
else:
    l=half; r=N; al=ah
while True:
    m=(l+r)//2
    am=ask(m%N)
    if am==al:
        l=m; al=am
    else:
        r=m
