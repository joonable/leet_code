def pickingNumbers(a):
    list_cnt = [0] * 100
    for num in a:
        list_cnt[num] += 1
    for i in range(1, len(list_cnt)):
        list_cnt[i - 1] += list_cnt[i]
    return max(list_cnt)