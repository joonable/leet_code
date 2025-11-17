def decentNumber(n):
    for i in range(n // 3, -1, -1):
        k = i * 3
        if (n - k) % 5 == 0:
            print(k * "5" + (n - k) * "3")
            return
    print(-1)
    return
