# TODO 오답내서 다시 풀어햐함
def solution(A):
    # (P, Q): A[P:Q + 1] 0 ≤ P < Q < N 
    # AVG(P, Q) = (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1)

    # [4,2,2,5,1,5,8] => 1
    # [2,1] => 0
    # [3,2,1] => 1
    # [10,-10,20] => 0
    # [-10,10,-20] => 0
    # [50,-10,20] => 1

    N = len(A)  # in [2..100,000]
    prefix_sum = [0] * (N + 1)
    for i, num in enumerate(A, 1):
        prefix_sum[i] = prefix_sum[i - 1] + num

    min_avg = float("inf")
    min_idx = 0
    for i in range(2, N + 1):
        avg = (prefix_sum[i] - prefix_sum[i - 2]) / 2
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 2

    if N > 2:
        for i in range(3, N + 1):
            avg = (prefix_sum[i] - prefix_sum[i - 3]) / 3
            if avg < min_avg:
                min_avg = avg
                min_idx = i - 3

    return min_idx

def solution(A):
    N = len(A)
    min_idx = 0
    min_avg = (A[0] + A[1]) / 2

    for i in range(N - 1):
        avg2 = (A[i] + A[i+1]) / 2
        if avg2 < min_avg:
            min_avg, min_idx = avg2, i
        if i + 2 < N:
            avg3 = (A[i] + A[i+1] + A[i+2]) / 3
            if avg3 < min_avg:
                min_avg, min_idx = avg3, i
    return min_idx