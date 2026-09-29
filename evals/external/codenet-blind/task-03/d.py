import itertools

def solve():
    D, G = map(int, input().split())
    problems = []
    for _ in range(D):
        p, c = map(int, input().split())
        problems.append((p, c))

    min_problems = float('inf')
    
    for mask in range(1 << D):
        total_score = 0
        total_problems = 0
        solved_complete = [False] * D

        # First solve complete sets
        for i in range(D):
            if mask & (1 << i):
                total_score += (i+1) * 100 * problems[i][0] + problems[i][1]
                total_problems += problems[i][0]
                solved_complete[i] = True

        # If needed, fill gaps with incomplete sets
        if total_score < G:
            for i in range(D-1, -1, -1):
                if not solved_complete[i]:
                    for j in range(problems[i][0]):
                        total_score += (i+1) * 100
                        total_problems += 1
                        if total_score >= G:
                            break
                    if total_score >= G:
                        break

        min_problems = min(min_problems, total_problems)

    print(min_problems)

solve()
