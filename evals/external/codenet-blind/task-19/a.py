Here's a solution to the problem:

from itertools import product

def is_normal_form(s):
    def is_isomorphic(s1, s2):
        if len(s1) != len(s2):
            return False
        s1_to_s2 = {}
        s2_to_s1 = {}
        for c1, c2 in zip(s1, s2):
            if c1 in s1_to_s2 and s1_to_s2[c1] != c2:
                return False
            if c2 in s2_to_s1 and s2_to_s1[c2] != c1:
                return False
            s1_to_s2[c1] = c2
            s2_to_s1[c2] = c1
        return True

    for t in product('abcdefghijklmnopqrstuvwxyz', repeat=len(s)):
        t = ''.join(t)
        if is_isomorphic(s, t) and t < s:
            return False
    return True

def generate_normal_form_strings(N):
    normal_form_strings = []
    for s in product('abcdefghijklmnopqrstuvwxyz', repeat=N):
        s = ''.join(s)
        if is_normal_form(s):
            normal_form_strings.append(s)
    return normal_form_strings

N = int(input())
result = generate_normal_form_strings(N)
print('\n'.join(result))
