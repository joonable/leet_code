# [3, 8, 9, 7, 6], 3 => [9, 7, 6, 3, 8]
# [0, 0, 0], 1 => [0, 0, 0]
# [1, 2, 3, 4], 4 => [1, 2, 3, 4]
# [9, 7, 6, 3, 8], 3 => [9, 7, 6, 3, 8]
# [], 4 => []
# [1], 4 => [1]

def solution(A, K):
    if not A:
        return A
    N = len(A)
    K = K % N
    return A[-K:] + A[:-K]

def solution_v2(A, K):
    N = len(A)
    if N == 0:
        return A
    K %= N
    if K == 0:
        return A
    return A[-K:] + A[:-K]