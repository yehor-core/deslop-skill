import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    pos = []
    neg = []
    zeros = []
    for x in A:
        if x > 0: pos.append(x)
        elif x < 0: neg.append(x)
        else: zeros.append(x)
    has_pos = len(pos) > 0
    has_neg = len(neg) > 0
    has_zero = len(zeros) > 0
    ops = []
    if len(zeros) == N:
        M = 0
        for _ in range(N-1):
            ops.append((0,0))
    elif (has_pos and has_neg) or (has_zero and (has_pos or has_neg)):
        if has_pos and has_neg:
            P1 = pos[:]
            N1 = neg[:]
        elif has_zero and has_pos:
            P1 = pos[:]
            N1 = zeros[:]
        else:
            P1 = zeros[:]
            N1 = neg[:]
        P1.sort()
        N1.sort()
        a = P1[0]
        del P1[0]
        b = N1[-1]
        del N1[-1]
        for n in N1:
            ops.append((a, n))
            a = a - n
        for p in P1:
            ops.append((b, p))
            b = b - p
        ops.append((a, b))
        M = a - b
    elif has_pos:
        arr = sorted(pos)
        mn = arr[0]
        arr_rem = arr[1:]
        a0 = arr_rem[-1]
        arr_rem2 = arr_rem[:-1]
        b0 = mn
        for x in arr_rem2:
            ops.append((b0, x))
            b0 = b0 - x
        ops.append((a0, b0))
        M = a0 - b0
    else:
        arr = sorted(neg, key=lambda x:abs(x))
        mn = arr[0]
        arr_rem = arr[1:]
        a0 = arr_rem[-1]
        arr_rem2 = arr_rem[:-1]
        b0 = mn
        for x in arr_rem2:
            ops.append((b0, x))
            b0 = b0 - x
        ops.append((b0, a0))
        M = b0 - a0
    w = sys.stdout.write
    w(str(M))
    w("\n")
    for x,y in ops:
        w(f"{x} {y}\n")
if __name__ == "__main__":
    main()
if False:
    pass
