# TODO 최적화 포인트 존재
def solution(A):
    # Implement your solution here
    # N = len(A) in [1..100,000]
    # [1, 3, 6, 4, 1, 2] => [1,1,2,3,4,6] => 5
    # [1, 3, 7, 4, 1, 2] => [1,1,2,3,4,7] => 5
    # [1,2,3,4,5,6,7] => 8
    # [1, 2, 3] => 4
    # [-1, -3] => [-3, -1] => 1

    result = 1
    A.sort()
    # print(A)
    for num in A:
        if num == result:
            result += 1
        elif num > result:
            return result
    return result


def solution(A):
    seen = set(A)
    result = 1
    while result in seen:
        result += 1
    return result