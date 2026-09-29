import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0]); K = int(data[1])
    A = list(map(int, data[2:]))
    MOD = 10**9+7
    pos = [x for x in A if x>0]
    neg = [x for x in A if x<0]
    zeros = A.count(0)
    if not pos and K%2==1:
        if zeros>0:
            print(0); return
        neg_sorted = sorted(neg, reverse=True)
        prod = 1
        for x in neg_sorted[:K]:
            prod = prod * (x%MOD) % MOD
        print(prod); return
    A.sort(key=lambda x: abs(x), reverse=True)
    S = A[:K]; T = A[K:]
    prod = 1
    negcnt = 0
    for x in S:
        if x==0:
            print(0); return
        if x<0: negcnt+=1
        prod = prod * (x%MOD) % MOD
    if negcnt%2==0:
        print(prod); return
    min_abs_neg_s = None; min_abs_pos_s = None
    for x in S:
        if x<0:
            if min_abs_neg_s is None or abs(x)<abs(min_abs_neg_s): min_abs_neg_s = x
        else:
            if min_abs_pos_s is None or abs(x)<abs(min_abs_pos_s): min_abs_pos_s = x
    max_abs_pos_t = None; max_abs_neg_t = None
    for x in T:
        if x>0:
            if max_abs_pos_t is None or abs(x)>abs(max_abs_pos_t): max_abs_pos_t = x
        elif x<0:
            if max_abs_neg_t is None or abs(x)>abs(max_abs_neg_t): max_abs_neg_t = x
    opt1 = min_abs_neg_s is not None and max_abs_pos_t is not None
    opt2 = min_abs_pos_s is not None and max_abs_neg_t is not None
    if not opt1 and not opt2:
        if zeros>0:
            print(0)
        else:
            print(prod)
        return
    if opt1 and opt2:
        left = abs(max_abs_pos_t) * abs(min_abs_pos_s)
        right = abs(max_abs_neg_t) * abs(min_abs_neg_s)
        if left > right:
            choose = 1
        else:
            choose = 2
    elif opt1:
        choose = 1
    else:
        choose = 2
    if choose==1:
        x = min_abs_neg_s; y = max_abs_pos_t
    else:
        x = min_abs_pos_s; y = max_abs_neg_t
    x_mod = x%MOD; y_mod = y%MOD
    inv_x = pow(x_mod, MOD-2, MOD)
    prod = prod * inv_x % MOD * y_mod % MOD
    print(prod)
if __name__ == "__main__":
    main()
