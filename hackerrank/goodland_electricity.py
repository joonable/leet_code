def pylons(k, arr):
    n = len(arr)
    curr = 0
    ans = 0

    while curr < n:
        left = max(0, curr - (k - 1))
        right = min(n - 1, curr + (k - 1))

        placed = -1
        for i in range(right, left - 1, -1):
            if arr[i] == 1:
                placed = i
                break

        if placed == -1:
            return -1

        ans += 1
        curr = placed + (k)

    return ans