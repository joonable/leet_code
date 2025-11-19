def biggerIsGreater(w):
    w = list(w)
    n = len(w)

    # 1) 뒤에서부터 pivot 찾기: w[i] < w[i+1]
    pivot = -1
    for i in range(n - 2, -1, -1):
        if w[i] < w[i + 1]:
            pivot = i
            break

    if pivot == -1:
        return "no answer"

    # 2) pivot보다 오른쪽에서 w[pivot]보다 큰 '가장 작은 문자' 찾기
    swap_index = pivot + 1
    for j in range(pivot + 2, n):
        if w[j] > w[pivot] and w[j] < w[swap_index]:
            swap_index = j

    # 3) swap
    w[pivot], w[swap_index] = w[swap_index], w[pivot]

    # 4) pivot 오른쪽 부분 정렬
    w[pivot + 1:] = sorted(w[pivot + 1:])

    return "".join(w)