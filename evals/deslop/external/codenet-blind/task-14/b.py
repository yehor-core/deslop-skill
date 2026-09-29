import sys
def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    C = [0]*N
    A = [None]*N
    for i in range(N):
        data = list(map(int, input().split()))
        C[i] = data[0]
        A[i] = data[1:]
    ans = 10**18
    for mask in range(1<<N):
        cost = 0
        skill = [0]*M
        for i in range(N):
            if mask >> i & 1:
                cost += C[i]
                if cost >= ans:
                    break
                for j in range(M):
                    skill[j] += A[i][j]
        else:
            if cost < ans and all(s >= X for s in skill):
                ans = cost
    if ans == 10**18:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
