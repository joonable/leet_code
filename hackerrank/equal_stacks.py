from heapq import heapify, heappop, heappush
from collections import deque
def equalStacks(h1, h2, h3):
    stacks = [deque(h1), deque(h2), deque(h3)]
    heights = [-sum(stack) for stack in stacks]
    heap = [(heights[0], 0), (heights[1], 1), (heights[2], 2)]
    heapify(heap)
    while not all([h == heights[0] for h in heights[1:]]):
        height, idx = heappop(heap)
        cylinder = stacks[idx].popleft()
        heights[idx] += cylinder
        heappush(heap, (heights[idx], idx))
    return -heights[0]