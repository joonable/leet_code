def solution(X, A):
    # Implement your solution here
    # init_pos = 0, target_pos = X + 1
    # N = len(A), A[K] = the position where one leaf falls at time K, measured in seconds.
    # N and X in  [1..100,000]
    # A[i] in [1..X]
    # no result => -1

    # (5, [1,3,1,4,2,3,5,4]) => 6
    # (5, [1,3,1,4,2,3,4,4]) => -1
    # (1, [1,3,1,4,2,3,4,4]) => 0
    # (5, [1,2,3,4,5]) => 4

    set_visited = set()
    for i, num in enumerate(A):
        set_visited.add(num)
        if len(set_visited) == X:
            return i
    return -1


def solution(X, A):
    # len(set) 호출 대신 단순 카운트 → 살짝 빠름
    seen = [False] * (X+1)
    remaining = X
    for i, pos in enumerate(A):
        if not seen[pos]:
            seen[pos] = True
            remaining -= 1
            if remaining == 0:
                return i
    return -1