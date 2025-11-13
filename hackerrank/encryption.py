from math import sqrt, ceil, floor


def encryption(s):
    s = "".join([ch for ch in s if ch != " "])
    n = len(s)
    rows = ceil(sqrt(n))
    cols = ceil(n / rows)
    result = [[""] * cols for _ in range(rows)]

    for i in range(n):
        ch = s[i]
        c = i // rows
        r = i - c * rows
        result[r][c] = ch
    return " ".join(["".join(r) for r in result])