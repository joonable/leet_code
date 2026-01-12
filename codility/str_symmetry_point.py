def solution(S):
    # Implement your solution here
    n = len(S)
    if n % 2 == 0:
        return -1

    l, r = 0, n - 1
    while l < r:
        if S[l] != S[r]:
            return -1
        l += 1
        r -= 1
    return (l + r) // 2