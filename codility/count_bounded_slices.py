from collections import deque

def solution(K, A):
    # Implement your solution here
    min_queue, max_queue = deque(), deque()

    n = len(A)
    l = 0
    result = 0
    for r in range(n):
        x = A[r]
        while min_queue and A[min_queue[-1]] > x:
            min_queue.pop()
        min_queue.append(r)

        while max_queue and A[max_queue[-1]] < x:
            max_queue.pop()
        max_queue.append(r)

        while A[max_queue[0]] - A[min_queue[0]] > K:
            if min_queue[0] == l:
                min_queue.popleft()
            if max_queue[0] == l:
                max_queue.popleft()
            l += 1

        result += r - l + 1
        if result > 1_000_000_000:
            return 1_000_000_000

    return result