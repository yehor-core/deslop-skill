import sys
import threading
def main():
    import sys
    from array import array
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    T = int(next(it))
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i] = int(next(it))
        B[i] = int(next(it))
    dpL = [array('I', [0]) * T for _ in range(N+1)]
    for i in range(N):
        a = A[i]; b = B[i]
        prev = dpL[i]; cur = dpL[i+1]
        # unroll t=0..a-1
        if a:
            for t in range(a):
                cur[t] = prev[t]
            for t in range(a, T):
                v1 = prev[t]; v2 = prev[t-a] + b
                cur[t] = v2 if v2 > v1 else v1
        else:
            for t in range(T):
                cur[t] = prev[t] + b
    dpR = [array('I', [0]) * T for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        a = A[i]; b = B[i]
        nxt = dpR[i+1]; cur = dpR[i]
        if a:
            for t in range(a):
                cur[t] = nxt[t]
            for t in range(a, T):
                v1 = nxt[t]; v2 = nxt[t-a] + b
                cur[t] = v2 if v2 > v1 else v1
        else:
            for t in range(T):
                cur[t] = nxt[t] + b
    ans = 0
    for i in range(N):
        best = 0
        L = dpL[i]; R = dpR[i+1]
        # combine L[t] + R[T-1-t]
        for l, r in zip(L, reversed(R)):
            s = l + r
            if s > best: best = s
        total = best + B[i]
        if total > ans: ans = total
    print(ans)

if __name__ == '__main__':
    main()
