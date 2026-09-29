import collections

def solve():
    n, m = map(int, input().split())
    adj = collections.defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    s, t = map(int, input().split())

    # State: (current_vertex, steps_in_ken_ken_pa)
    # steps_in_ken_ken_pa ranges from 0 to 2
    # 0: at the start of a ken-ken-pa, ready to take the first step
    # 1: after the first step, ready to take the second step
    # 2: after the second step, ready to take the third step
    # Reaching a vertex after the third step completes a ken-ken-pa

    # Distance: dist[vertex][steps_in_ken_ken_pa]
    dist = [[-1] * 3 for _ in range(n + 1)]

    q = collections.deque()

    # Initial state: at vertex S, 0 steps into the current ken-ken-pa
    dist[s][0] = 0
    q.append((s, 0))

    while q:
        curr_v, curr_step = q.popleft()

        if curr_step == 2: # Just completed a full ken-ken-pa
            next_step = 0
            next_ken_ken_pas = dist[curr_v][curr_step] + 1
            if dist[curr_v][next_step] == -1:
                dist[curr_v][next_step] = next_ken_ken_pas
                q.append((curr_v, next_step))
        else: # Continuing the current ken-ken-pa
            next_step = curr_step + 1
            for neighbor in adj[curr_v]:
                if dist[neighbor][next_step] == -1:
                    dist[neighbor][next_step] = dist[curr_v][curr_step]
                    q.append((neighbor, next_step))

    # We want to reach vertex T after completing a ken-ken-pa (i.e., after 3 steps)
    # This corresponds to the state (T, 0) in our distance array, which stores the number of full ken-ken-pas completed.
    # So we are looking for dist[t][0]
    print(dist[t][0])

solve()
```
