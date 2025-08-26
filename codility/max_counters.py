# TODO hint
def solution(N, A):
    # Implement your solution here
    # M = len(A)
    # N, M in [1..100,000]
    # 각각 다 더한 다음에 마지막에 maxcounter를 더하면 어케되지

    # (5, [3,4,4,6,1,4,4]) => [3, 2, 2, 4, 2]
    # (1, [1,2,1,2]) => [2]

    max_num = 0
    base = 0
    counters = [0] * N
    for num in A:
        if num == N + 1:
            base = max_num
        else:
            counters[num - 1] = max(counters[num - 1], base) + 1
            max_num = max(max_num, counters[num - 1])

    for i in range(N):
        counters[i] = max(counters[i], base)

    return counters