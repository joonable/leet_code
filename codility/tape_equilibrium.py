def solution(A):
    # Implement your solution here
    # N = len(A), such that N in [2..100,000]
    # 0 < P < N
    # result: absolute difference between the sum of the first part and the sum of the second part
    # [3, 1, 2, 4, 3] => [7, 4, 1, 7] => 1
    # [3, 1, 2, 4, 3] => [4, 1, 5, 13] => 1
    # [1, 1] => [0] => 0
    # [1, -2] => [3] => 3
    # [-1, 2] => [3] => 3
    # [-1, -3] => [2] => 2
    # [10, 2] => [8] => 8
    # [-10, 2] => [12] => 12

    N = len(A)
    first_sum = 0
    second_sum = sum(A)
    min_diff = float("inf")

    for i in range(N - 1):
        first_sum += A[i]
        second_sum -= A[i]
        min_diff = min(min_diff, abs(first_sum - second_sum))

    return min_diff


def solution_v2(A):
    total = sum(A)
    left = 0
    min_diff = float("inf")
    for i in range(len(A)-1):
        left += A[i]
        diff = abs(left - (total - left))
        min_diff = min(min_diff, diff)
    return min_diff