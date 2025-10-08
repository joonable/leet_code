from collections import Counter
def solution(participant, completion):
    answer = ''
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    for k, v in counter_c.items():
        counter_p[k] -= v
        if counter_p[k] != 0:
            return k
        else:
            del counter_p[k]
    return list(counter_p.keys())[0]