def substrings(n):
    MOD = 10**9 + 7
    len_n = len(n)

    # dp[i] = i번째 글자에서 끝나는 모든 substring들의 합
    # (dp[1] = digit1, dp[2] = digit2 + 12, dp[3] = 3 + 23 + 123, ...)
    dp = [0] * (len_n + 1)

    for i in range(1, len_n + 1):
        digit = int(n[i - 1])
        # 점화식:
        # dp[i] =
        # dp[i-1] * 10 → 기존 substring 뒤에 digit 붙이기
        # + digit * i → digit 혼자 생성하는 i개의 substring
        dp[i] = (dp[i - 1] * 10 + digit * i) % MOD

    return sum(dp) % MOD