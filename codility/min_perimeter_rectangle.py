import math
def solution(N):
    for d in range(int(math.sqrt(N)) + 1 + 1, 0, -1):
        m, r = divmod(N, d)
        if r == 0:
            return 2 * (m + d)
    return -1