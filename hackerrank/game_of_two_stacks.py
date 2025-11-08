from itertools import accumulate


def twoStacks(maxSum, a, b):
    acc_a = [0] + list(accumulate(a))
    acc_b = [0] + list(accumulate(b))
    m, n = len(acc_a), len(acc_b)

    b_count = 0
    while b_count < n and acc_b[b_count] <= maxSum:
        b_count += 1
    b_count -= 1

    result = b_count

    for a_count in range(1, m):
        if acc_a[a_count] > maxSum:
            break
        while b_count >= 0 and acc_a[a_count] + acc_b[b_count] > maxSum:
            b_count -= 1
        result = max(result, a_count + b_count)
    return result