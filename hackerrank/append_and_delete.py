def appendAndDelete(s, t, k):
    m, n = len(s), len(t)

    # Case 1: k가 너무 커서 전부 지우고 다시 쓰는 것이 가능
    if k >= m + n:
        return "Yes"

    # 공통 prefix 길이 찾기
    common = 0
    for ch_s, ch_t in zip(s, t):
        if ch_s != ch_t:
            break
        common += 1

    # 필요한 delete, append 계산
    delete_ops = m - common
    append_ops = n - common
    total_ops = delete_ops + append_ops

    # Case 2: 총 필요한 조작보다 k가 부족 → 불가능
    if total_ops > k:
        return "No"

    # Case 3: 정확히 맞아떨어짐 → 가능
    if (k - total_ops) % 2 == 0:
        return "Yes"

    # Case 4: 조작 후 남은 k가 홀수 → 불가능
    return "No"