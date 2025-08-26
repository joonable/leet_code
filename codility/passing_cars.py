def solution(A):
    # N = len(A), [1..100,000]
    # A[i] in [0:east, 1:west]
    # result = passing cars
    # (P, Q), where 0 ≤ P < Q < N

    # [0,1,0,1,1] => (0, 1), (0, 3), (0, 4), (2, 3), (2, 4) => 5
    # [0] => 0
    # [1] => 0
    # [0,0] => 0
    # [1,1] => 0
    # [0,1] => 1
    # [1,0] => 0

    result = 0
    n_car_east = 0

    for direction in A:
        if direction == 0:
            n_car_east += 1
        else:
            result += n_car_east
            if result > 1_000_000_000:
                return -1
    return result


