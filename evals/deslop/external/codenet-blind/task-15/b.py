```python
import sys

sys.setrecursionlimit(210000)
MOD = 1000000007


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)


def normalize(a, b):
  if a == 0 and b == 0:
    return (0, 0)
  if a == 0:
    return (0, 1 if b > 0 else -1)
  if b == 0:
    return (1 if a > 0 else -1, 0)
  g = gcd(abs(a), abs(b))
  a //= g
  b //= g
  if a < 0 or (a == 0 and b < 0):
    a *= -1
    b *= -1
  return (a, b)


def solve():
  N = int(sys.stdin.readline())
  sardines = []
  for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    sardines.append((A, B))

  groups = {}
  independent_count = 0

  for A, B in sardines:
    if A == 0 and B == 0:
      independent_count += 1
      continue
    norm_a, norm_b = normalize(A, B)
    if (norm_a, norm_b) not in groups:
      groups[(norm_a, norm_b)] = []
    groups[(norm_a, norm_b)].append((A, B))

  total_ways = 1

  for key in groups:
    g1 = groups[key]
    a1, b1 = key

    count = len(g1)
    valid_combinations = 0

    if a1 == 0 and b1 == 1:
      valid_combinations = (1 << count) - 1
    elif a1 == 0 and b1 == -1:
      valid_combinations = (1 << count) - 1
    elif a1 == 1 and b1 == 0:
      valid_combinations = (1 << count) - 1
    elif a1 == -1 and b1 == 0:
      valid_combinations = (1 << count) - 1
    else:
      complement_key = (-a1, -b1)
      if complement_key in groups:
        g2 = groups[complement_key]
        count_complement = len(g2)

        # Combinations within g1
        valid_combinations += (1 << count) - 1

        # Combinations within g2
        valid_combinations += (1 << count_complement) - 1

        # Combinations of one from g1 and one from g2
        for s1_a, s1_b in g1:
          for s2_a, s2_b in g2:
            if s1_a * s2_a + s1_b * s2_b == 0:
              valid_combinations += 1
      else:
        valid_combinations = (1 << count) - 1

    total_ways = (total_ways * (valid_combinations + 1)) % MOD

  total_ways = (total_ways * ((1 << independent_count) - 1 + 1)) % MOD
  print(total_ways)


solve()
```
