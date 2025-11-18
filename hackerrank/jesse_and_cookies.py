from heapq import heapify, heappush, heappop
def cookies(k, A):
    heap = A
    heapify(heap)
    result = 0
    while len(heap) >= 2:
        if heap[0] >= k:
            return result
        result += 1
        f_cookie = heappop(heap)
        s_cookie = heappop(heap)
        n_cookie = f_cookie + 2 * s_cookie
        heappush(heap, n_cookie)
    return result if heap[0] >= k else -1