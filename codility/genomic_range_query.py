def solution(S, P, Q):
    # ("CAGCCTA", [2,5,0], [4,5,6]) => [2,4,1]
    # [2..4] => [GCC] => [322] => 2
    # [5..5] => [T] => [4] => 4
    # [0..6] => [CAGCCTA] => [2132241] => 1

    N, M = len(S), len(P)

    prefix_count_a = [0] * (N + 1)
    prefix_count_c = [0] * (N + 1)
    prefix_count_g = [0] * (N + 1)

    for i in range(1, N + 1):
        ch = S[i - 1]
        prefix_count_a[i] = prefix_count_a[i - 1] + (ch == "A")
        prefix_count_c[i] = prefix_count_c[i - 1] + (ch == "C")
        prefix_count_g[i] = prefix_count_g[i - 1] + (ch == "G")

    result = []
    for p, q in zip(P, Q):
        if prefix_count_a[q + 1] - prefix_count_a[p] > 0:
            result.append(1)
        elif prefix_count_c[q + 1] - prefix_count_c[p] > 0:
            result.append(2)
        elif prefix_count_g[q + 1] - prefix_count_g[p] > 0:
            result.append(3)
        else:
            result.append(4)
    return result