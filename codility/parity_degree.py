from math import log2
def solution(N):
    # Implement your solution here
    for i in range(int(log2(N)), 0, -1):
        if N % (2 ** i) == 0:
            return i
    return 0