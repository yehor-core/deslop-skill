import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    c = [0] * (n + 1)
    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        c[a] ^= 1
        c[b] ^= 1
    for i in range(1, n + 1):
        if c[i]:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    threading.Thread(target=main).start()
