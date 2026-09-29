import itertools

def solve():
    N, M, X = map(int, input().split())
    books = []
    for _ in range(N):
        line = list(map(int, input().split()))
        cost = line[0]
        skills = line[1:]
        books.append((cost, skills))

    min_cost = float('inf')
    possible = False

    for i in range(1 << N):
        current_cost = 0
        current_skills = [0] * M

        for j in range(N):
            if (i >> j) & 1:
                current_cost += books[j][0]
                for k in range(M):
                    current_skills[k] += books[j][1][k]

        all_skills_met = True
        for skill_level in current_skills:
            if skill_level < X:
                all_skills_met = False
                break

        if all_skills_met:
            possible = True
            min_cost = min(min_cost, current_cost)

    if possible:
        print(min_cost)
    else:
        print(-1)

solve()
