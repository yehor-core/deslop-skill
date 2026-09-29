import sys
import threading
def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    al = []
    bl = []
    for _ in range(N):
        s = input().strip()
        bal = 0
        minbal = 0
        for c in s:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < minbal:
                minbal = bal
        if bal >= 0:
            al.append((minbal, bal))
        else:
            rbal = 0
            rmin = 0
            for c in reversed(s):
                if c == ')':
                    rbal += 1
                else:
                    rbal -= 1
                if rbal < rmin:
                    rmin = rbal
            bl.append((rmin, bal))
    al.sort(key=lambda x: -x[0])
    bl.sort(key=lambda x: -x[0])
    cur = 0
    for mb, b in al:
        if cur + mb < 0:
            print("No")
            return
        cur += b
    for mb, b in bl:
        if cur + mb < 0:
            print("No")
            return
        cur += b
    print("Yes" if cur == 0 else "No")

if __name__ == "__main__":
    main()
