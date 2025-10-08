from collections import defaultdict
def solution(clothes):
    counter = defaultdict(int)
    for nm, tp in clothes:
        counter[tp] += 1
    answer = 1
    for val in counter.values():
        answer *= (val + 1)
    return answer - 1