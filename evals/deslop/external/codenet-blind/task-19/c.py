```python
import sys

input = sys.stdin.readline
N = int(input())


def is_isomorphic(s, t):
  if len(s) != len(t):
    return False
  d1 = {}
  d2 = {}
  for i in range(len(s)):
    if s[i] not in d1:
      d1[s[i]] = t[i]
    elif d1[s[i]] != t[i]:
      return False
    if t[i] not in d2:
      d2[t[i]] = s[i]
    elif d2[t[i]] != s[i]:
      return False
  return True


def solve(k, current, mapping):
  if k == N:
    s = ''
    for c in current:
      s += c
    return [s]
  res = []
  used_chars = set()
  for c in current:
    used_chars.add(mapping[c])
  for char_code in range(ord('a'), ord('z') + 1):
    char = chr(char_code)
    if char not in used_chars:
      new_mapping = mapping.copy()
      new_mapping[k] = char
      res.extend(solve(k + 1, current + [char], new_mapping))
  return res


ans = []


def check(s):
  for i in range(len(s)):
    for j in range(len(s)):
      if s[i] == s[j] and s[i] != s[j]:
        return False
      if s[i] != s[j] and s[i] == s[j]:
        return False
  return True


def generate(k, current, mapping, used_mapping):
  if k == N:
    s = ''
    for c in current:
      s += c
    is_normal = True
    for i in range(1 << N):
      t = ''
      temp_mapping = {}
      temp_used_mapping = set()
      valid = True
      for j in range(N):
        if (i >> j) & 1:
          if s[j] not in temp_mapping:
            temp_mapping[s[j]] = chr(ord('a') + j)
          else:
            if temp_mapping[s[j]] != chr(ord('a') + j):
              valid = False
              break
          if chr(ord('a') + j) in temp_used_mapping:
            valid = False
            break
          temp_used_mapping.add(chr(ord('a') + j))
        else:
          if s[j] in temp_mapping:
            t += temp_mapping[s[j]]
          else:
            for char_code in range(ord('a'), ord('z') + 1):
              char = chr(char_code)
              if char not in temp_used_mapping:
                temp_mapping[s[j]] = char
                temp_used_mapping.add(char)
                break
            t += temp_mapping[s[j]]
      if not valid:
        continue
      if is_isomorphic(s, t) and s > t:
        is_normal = False
        break
    if is_normal:
      ans.append(s)
    return
  for char_code in range(ord('a'), ord('z') + 1):
    char = chr(char_code)
    if k not in mapping:
      if char in used_mapping:
        continue
      new_mapping = mapping.copy()
      new_used_mapping = used_mapping.copy()
      new_mapping[k] = char
      new_used_mapping.add(char)
      generate(k + 1, current + [char], new_mapping, new_used_mapping)
    else:
      if mapping[k] == char:
        generate(k + 1, current + [char], mapping.copy(), used_mapping.copy())


mapping = {}
used_mapping = set()
generate(0, [], mapping, used_mapping)
ans.sort()
for s in ans:
  print(s)
```
