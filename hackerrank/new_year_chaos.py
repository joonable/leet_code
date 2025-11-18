def minimumBribes(q):
    brides = 0
    for i, x in enumerate(q):
        if x - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(x - 2, 0), i):
            y = q[j]
            if y > x:
                brides += 1
    print(brides)