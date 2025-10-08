def solution(brown, yellow):
    n = brown + yellow
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0 and yellow == (i - 2) * (n // i - 2):
            return [n // i, i]