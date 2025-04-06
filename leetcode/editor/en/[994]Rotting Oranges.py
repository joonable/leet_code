from collections import deque

from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        def get_directions(r, c):
            return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in get_directions(r, c):
                    if is_valid(nr, nc):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if fresh == 0 else -1