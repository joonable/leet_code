def solution(A):
    count = 0
    idx = 0

    while idx != -1:
        count += 1
        idx = A[idx]

    return count