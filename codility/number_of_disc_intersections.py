# TODO 힌트 받음
def solution(A):
    # [1,5,2,1,4,0] => 11
    # left_points: [-4, -1, 0, 0, 2, 5]
    # right_points: [1, 4, 4, 5, 6, 8]
    # [-4, -1, 0, 0, 2, 5]
    # [1, 4, 4, 5, 6, 8]

    # [0, 0, 0] => 0
    # [1, 1, 0] => 2
    # [1, 1, 1] => 3
    # [100, 1, 1] => 3

    N = len(A)
    left_points = sorted([c - r for c, r in enumerate(A)])
    right_points = sorted([c + r for c, r in enumerate(A)])

    left, right = 0, 0
    activate = 0
    result = 0

    while left < N:
        if left_points[left] <= right_points[right]:
            result += activate
            if result > 10_000_000:
                return -1
            left += 1
            activate += 1
        else:
            right += 1
            activate -= 1
    return result