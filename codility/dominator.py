# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    # dominator: occurs in more than half
    # [3,4,3,2,3,-1,3,3] => 3
    # [1,1,2,2] => 0
    # [1,1,2,2,2] => 4
    if not A:
        return -1

    N = len(A)
    dict_counter = defaultdict(int)
    target = N // 2 # in [0..100_000]
    for i, num in enumerate(A):
        dict_counter[num] += 1
        if target < dict_counter[num]:
            return i
    return -1

from collections import defaultdict

def solution(A):
    N = len(A)
    if N == 0:
        return -1

    counts = defaultdict(int)
    for num in A:
        counts[num] += 1
        if counts[num] > N // 2:
            # dominator value found
            dominator = num
            break
    else:   # 루프가 끝날 때까지 break가 없었다면 dominator가 없음
        return -1

    # dominator 확인 완료 후 인덱스 아무거나 리턴
    for i, v in enumerate(A):
        if v == dominator:
            return i
    return -1
