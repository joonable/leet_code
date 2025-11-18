from collections import Counter


def isValid_v1(s):
    counter = Counter(s)
    list_cnt = counter.values()
    min_cnt = min(list_cnt)
    flag1 = sum([cnt - min_cnt for cnt in list_cnt]) in [0, 1]
    if flag1:
        return "YES"

    cnt_counter = Counter(list_cnt)
    return "YES" if len(cnt_counter) == 2 and (1, 1) in list(cnt_counter.items()) else "NO"


def isValid_v2(s):
    freq = Counter(s)
    values = list(freq.values())
    freq_counts = Counter(values)

    # 1) 모든 문자가 동일 빈도
    if len(freq_counts) == 1:
        return "YES"

    # 2) 두 종류의 freq일 때만 가능성 있음
    if len(freq_counts) > 2:
        return "NO"

    # freqCounts example: {3:1, 2:4}
    (f1, c1), (f2, c2) = freq_counts.items()

    # 작은 freq, 큰 freq 정렬
    small_f, small_c = (f1, c1) if f1 < f2 else (f2, c2)
    big_f, big_c = (f2, c2) if f1 < f2 else (f1, c1)

    # Case 1: 작은 freq가 1이고 딱 1개만 있다
    if small_f == 1 and small_c == 1:
        return "YES"

    # Case 2: 큰 freq가 작은 freq + 1 이고, 큰 freq는 딱 하나만 존재
    if big_f == small_f + 1 and big_c == 1:
        return "YES"

    return "NO"