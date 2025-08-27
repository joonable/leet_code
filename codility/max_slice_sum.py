# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # (P, Q) = sum(A[P:Q+1])
    # return maximum sum of any slice of A
    # [3,2,-6,4,0] = # [3,5,5,5(4),5(4)] = 5

    # [3,2,-6,10,4] # [3,5,5,10,14] = 14
    # [3,2,-1,10] # [3,5,5,14] = 14
    # [-1,2,-1,10] = 11
    # [-1,2,2,11] = 15
    # [-2,-1,-3] = -1
    # [-1,-2,-3] = -1
    # [-1,-2,-3] = -1
    # [0,0,0] = 0

    # N = len(A) # from 1

    max_sum = -float("inf")
    min_prefix = 0
    curr_sum = 0
    for num in A:
        curr_sum += num
        max_sum = max(max_sum, curr_sum - min_prefix)
        min_prefix = min(min_prefix, curr_sum)
    return max_sum


# TODO 이거 봐야함
def solution(A):
    """
    Count Equi Leaders.
    An index S (0 <= S < N-1) is an equi leader if A[:S+1] and A[S+1:] share the same leader.
    Time: O(N), Space: O(1) extra (besides input).
    """

    N = len(A)
    if N < 2:
        return 0

    # 1) Find dominator candidate by Boyer–Moore
    size = 0
    candidate = None
    for x in A:
        if size == 0:
            candidate = x
            size = 1
        elif x == candidate:
            size += 1
        else:
            size -= 1

    # 2) Verify candidate is dominator (occurs > N/2)
    total = 0
    for x in A:
        if x == candidate:
            total += 1
    if total * 2 <= N:
        return 0  # no dominator => no equi leader

    # 3) Sweep once; count equi leaders using prefix count of candidate
    equi = 0
    left_cnt = 0  # count of candidate in A[:i+1]
    for i, x in enumerate(A[:-1]):        # S = i, only up to N-2
        if x == candidate:
            left_cnt += 1
        left_len = i + 1
        right_len = N - left_len
        right_cnt = total - left_cnt
        if left_cnt * 2 > left_len and right_cnt * 2 > right_len:
            equi += 1

    return equi