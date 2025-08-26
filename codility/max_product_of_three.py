# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
################TODO 힌트 받음
import math

def solution(A):
    # Implement your solution here
    # N = len(A) # in [3..100,000]
    # (P, Q, R) = A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
    # [-3,1,2-2,5,6] = 60
    # [-4,-3,-2,-1] = -6
    # [-4,-3,-2,1] = 12
    # [-4,-3,1,2] = 24
    # [-3,-2,1] = 6
    # [-3,1,2] = -6
    # [-3,-2,-1,100,200] = 1200ㅜ
    # [-5,-2,3,4,5] = 60
    # [-3,-2,-1,2,3] = 18

    A.sort()

    # 맨 앞 음수 2 X 맨뒤 양수 1
    first_one_last_two = math.prod(A[:2]) * A[-1]

    # 맨뒤 양수 3
    last_three = math.prod(A[-3:])

    return max(first_one_last_two, last_three)

