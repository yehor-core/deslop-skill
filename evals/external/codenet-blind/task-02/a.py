import itertools

def solve(N, A, B, values):
    max_mean = float('-inf')
    max_mean_ways = 0

    for count in range(A, B + 1):
        for combination in itertools.combinations(values, count):
            current_mean = sum(combination) / count
            
            if current_mean > max_mean:
                max_mean = current_mean
                max_mean_ways = 1
            elif current_mean == max_mean:
                max_mean_ways += 1

    return max_mean, max_mean_ways

def main():
    N, A, B = map(int, input().split())
    values = list(map(int, input().split()))
    
    max_mean, max_mean_ways = solve(N, A, B, values)
    
    print(f"{max_mean:.6f}")
    print(max_mean_ways)

if __name__ == "__main__":
    main()
