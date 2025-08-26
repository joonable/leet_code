from math import ceil

def solution(X, Y, D):
    # Implement your solution here
    # X = curr_pos, Y = target_pos, D = jump
    # such that X ≤ Y, [1..1,000,000,000]
    # 10, 85, 30 => 3
    # 80, 80, 30 => 0
    # 10, 20, 10 => 1
    # 1, 10, 1 => 9
    # 1, 1000000000, 1 => 999999999

    if X == Y:
        return 0
    else:
        return ceil((Y - X) / D)

def solution_v2(X, Y, D):
    # X ≤ Y, D ≥ 1 가정 (문제 제약)
    # (a + b - 1) // b는 ceil(a / b)와 동치 such that (a, b > 0)
    return 0 if X == Y else (Y - X + D - 1) // D