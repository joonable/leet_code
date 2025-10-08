# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import accumulate

def solution(A):
    # A[i]: stock price on the i-th day
    # result: the maximum possible profit
    # [23171,21011,21123,21366,21013,21367] => 21367-21011 => 256
    # [] => 0
    # [2,1] => 0
    # [1,2] => 1
    # [1,2,4] => 2
    # [2,2,4] => 2
    # [2,1,4] => 3

    if not A:
        return 0

    # N = len(A)
    curr_min = float("inf")
    max_profit = 0
    for price in A:
        curr_min = min(price, curr_min)
        max_profit = max(max_profit, price - curr_min)
    return max_profit if max_profit > 0 else 0
