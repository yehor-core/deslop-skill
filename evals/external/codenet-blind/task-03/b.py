import sys

def solve():
    D, G = map(int, sys.stdin.readline().split())
    problems = []
    for i in range(D):
        p, c = map(int, sys.stdin.readline().split())
        problems.append((p, c, (i + 1) * 100))

    min_problems = float('inf')

    for i in range(1 << D):
        current_score = 0
        current_problems_count = 0
        
        for j in range(D):
            if (i >> j) & 1:
                p, c, score_val = problems[j]
                current_score += p * score_val + c
                current_problems_count += p
        
        if current_score >= G:
            min_problems = min(min_problems, current_problems_count)
            continue
        
        remaining_needed = G - current_score
        
        for j in range(D - 1, -1, -1):
            if not ((i >> j) & 1):
                p, c, score_val = problems[j]
                
                num_to_solve = (remaining_needed + score_val - 1) // score_val
                
                if num_to_solve <= p:
                    min_problems = min(min_problems, current_problems_count + num_to_solve)
                    break
                else:
                    current_score += p * score_val
                    current_problems_count += p
                    remaining_needed = G - current_score
                    if current_score >= G:
                        min_problems = min(min_problems, current_problems_count)
                        break
    print(min_problems)

solve()
```
