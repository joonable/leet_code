def candies(n, arr):
    n_candies = [1] * n
    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            n_candies[i] = n_candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            n_candies[i] = max(n_candies[i], n_candies[i + 1] + 1)
    return sum(n_candies)