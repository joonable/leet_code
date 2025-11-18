def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for query in queries:
        op, x, y = query
        if op == 1:
            idx = (x ^ last_answer) % n
            arr[idx].append(y)
        else:
            idx = (x ^ last_answer) % n
            last_answer = arr[idx][y % len(arr[idx])]
            result.append(last_answer)
    return result