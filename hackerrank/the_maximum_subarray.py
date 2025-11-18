def maxSubarray(arr):
    current = 0
    result1 = -float("inf")
    result2 = 0
    has_positive = False
    for i in range(len(arr)):
        current = max(arr[i], current + arr[i])
        result1 = max(result1, current)
        if arr[i] >= 0:
            has_positive = True
            result2 += arr[i]

    if not has_positive:
        result2 = max(arr)
    return [result1, result2]