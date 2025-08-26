# TODO 오답
def solution(A):
    # Implement your solution here
    # N = len(A) in [1..100,000
    # result = 1 if permutation else 0

    # [4,1,3,2] => 1
    # [4,1,3] => 0
    # [1,2,3] => 1
    # [1,3,3] => 0
    # [1] => 1
    # [2] => 1
    # [2,6] => 0

    N = len(A)
    set_visited = set()
    min_num, max_num = float("inf"), 0
    for num in A:
        if num in set_visited or num >= min_num + N:
            return 0
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        set_visited.add(num)
    return 1 if max_num - min_num + 1 == N else 0


def solution(A):
    N = len(A)
    set_visited = set()
    for num in A:
        if num in set_visited or not (1 <= num <= N):
            return 0
        set_visited.add(num)
    return 1
