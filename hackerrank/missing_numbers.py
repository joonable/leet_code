from collections import Counter


def missingNumbers(arr, brr):
    # Write your code here
    counter_a = Counter(arr)
    counter_b = Counter(brr)
    for num, cnt in counter_a.items():
        counter_b[num] -= counter_a[num]
        if counter_b[num] == 0:
            del counter_b[num]

    result = []
    for num, cnt in counter_b.items():
        if cnt > 0:
            result.append(num)
    result.sort()
    return result
