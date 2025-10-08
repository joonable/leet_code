from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    list_permutations = list(permutations(range(n), n))
    max_result = -1
    for permutation in list_permutations:
        result = 0
        curr_k = k
        for idx in permutation:
            if curr_k >= dungeons[idx][0]:
                curr_k -= dungeons[idx][1]
                result += 1
                max_result = max(result, max_result)
    return max_result