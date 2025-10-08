from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        sco1 = heappop(scoville)
        sco2 = heappop(scoville)
        heappush(scoville, sco1 + sco2 * 2)
        answer += 1
    return answer if scoville[0] >= K else -1