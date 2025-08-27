from collections import deque

def solution(K, A):
    n = len(A)
    minDQ, maxDQ = deque(), deque()
    L = 0
    ans = 0
    CAP = 1_000_000_000  # 있으면 사용, 없으면 제거

    for R, x in enumerate(A):
        # 업데이트: 단조 데크 유지
        while minDQ and A[minDQ[-1]] > x:
            minDQ.pop()
        minDQ.append(R)

        while maxDQ and A[maxDQ[-1]] < x:
            maxDQ.pop()
        maxDQ.append(R)

        # 조건 위반 시 L 이동
        while A[maxDQ[0]] - A[minDQ[0]] > K:
            if minDQ[0] == L:
                minDQ.popleft()
            if maxDQ[0] == L:
                maxDQ.popleft()
            L += 1

        ans += R - L + 1
        if ans > CAP:
            return CAP

    return ans