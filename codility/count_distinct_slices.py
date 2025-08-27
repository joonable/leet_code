# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # (P,Q) = A[P:Q+1]
    # (6, [3, 4, 5, 5, 2]) = 9
    # (6, [1, 1, 1]) = 3
    # (6, [5, 5, 1, 5]) = 6
    # (6, [1, 3, 1, 3]) = 7
    # (6, [1, 3, 3, 1]) = 6

    N = len(A)
    set_seen = set()
    # set_temp = {}
    l = 0
    result = 0
    for r in range(N):
        r_num = A[r]
        while r_num in set_seen:
            set_seen.remove(A[l])
            l += 1
        set_seen.add(A[r])
        result += (r - l + 1)
        if result > 1_000_000_000:
            return 1_000_000_000
    return result

