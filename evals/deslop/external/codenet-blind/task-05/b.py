
from math import factorial
# 組み合わせ
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

def main():
    num, k = map(int, input().split())

    max_num = combinations_count(num - 1, 2)

    if k > max_num:
        print('-1')
    else:
        edge = num - 1
        now_count = max_num
        data = [[num, i] for i in range(1, num)]
        for i in range(1, num):
            for j in range(i + 1, num):
                if now_count > k:
                    edge += 1
                    now_count -= 1
                    data.append([i, j])
                else:
                    pass

        print(edge)
        for i, j in data:
            print(i, j)

if __name__ == '__main__':
    main()
