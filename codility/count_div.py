# TODO 오답
def solution(A, B, K):
    # A, B in [0..2,000,000,000], A <= B
    # K in  [1..2,000,000,000
    # result: x % K == 0, x in [A..B]

    # 6,11,2 => 6,8,10 => 3
    # 0,2000000000,1 =>
    # 0,0,2000000000 => 1
    # 1,1,2000000000 => 0
    # 1,1,1 => 1
    # 1,2,1 => 2
    # 1,2,3 => 0
    # 7,11,5 => 1

    b_count = B // K
    a_count = A // K
    result = b_count - a_count
    return result if A % K != 0 else result + 1


def solution(A, B, K):
    # 개수 = [0..B]까지의 배수 개수 - [0..A-1]까지의 배수 개수
    return B // K - (A - 1) // K