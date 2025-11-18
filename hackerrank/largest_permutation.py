def largestPermutation(k, arr):
    n = len(arr)
    pos = {value: idx for idx, value in enumerate(arr)}

    for i in range(n):
        if k == 0:
            break

        wanted = n - i
        current = arr[i]
        if current == wanted:
            continue

        swap_idx = pos[wanted]
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

        pos[current] = swap_idx
        pos[wanted] = i

        k -= 1

    return arr