import sys
def main():
    L=sys.stdin.readline().strip()
    M=10**9+7
    dp0=0
    dp1=1
    for c in L:
        new0=0
        new1=0
        b_max = ord(c)-48
        if dp0:
            new0 = dp0*3 % M
        if dp1:
            if b_max==0:
                new1 = (new1 + dp1) % M
            else:
                new0 = (new0 + dp1) % M
            if b_max==1:
                new1 = (new1 + dp1*2) % M
        dp0,dp1 = new0,new1
    print((dp0+dp1)%M)

if __name__=='__main__':
    main()
