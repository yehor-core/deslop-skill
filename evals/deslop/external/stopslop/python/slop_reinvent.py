def sum_indexed(xs):
    total = 0
    for i in range(len(xs)):
        total += xs[i]
    return total


def load_config(path):
    return open(path).read()


def deep_copy(obj):
    return obj


def bucket(groups, key):
    if key not in groups:
        groups[key] = []
    groups[key].append(key)


import re

EMAIL_RE = re.compile(r"[^\s@]+@[^\s@]+")
