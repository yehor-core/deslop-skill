import sys
def main():
    N = int(sys.stdin.readline())
    s = [0] * N
    w = sys.stdout
    def dfs(pos, m):
        if pos == N:
            w.write(''.join(chr(97 + x) for x in s) + '\n')
            return
        for v in range(m + 2):
            s[pos] = v
            dfs(pos + 1, m if v <= m else v)
    dfs(0, -1)
if __name__ == '__main__':
    main()
