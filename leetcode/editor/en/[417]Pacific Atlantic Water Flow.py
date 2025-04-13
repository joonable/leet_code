# There is an m x n rectangular island that borders both the Pacific Ocean and 
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and 
# the Atlantic Ocean touches the island's right and bottom edges. 
# 
#  The island is partitioned into a grid of square cells. You are given an m x 
# n integer matrix heights where heights[r][c] represents the height above sea 
# level of the cell at coordinate (r, c). 
# 
#  The island receives a lot of rain, and the rain water can flow to 
# neighboring cells directly north, south, east, and west if the neighboring cell's height 
# is less than or equal to the current cell's height. Water can flow from any cell 
# adjacent to an ocean into the ocean. 
# 
#  Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic 
# oceans. 
# 
#  
#  Example 1: 
#  
#  
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, 
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the 
# Pacific and Atlantic oceans.
#  
# 
#  Example 2: 
# 
#  
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and 
# Atlantic oceans.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == heights.length 
#  n == heights[r].length 
#  1 <= m, n <= 200 
#  0 <= heights[r][c] <= 10⁵ 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Matrix 👍 7771 ?
# ? 1584


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List

# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         def get_neighbours(r, c):
#             return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

#         def is_valid(r, c):
#             nonlocal rows, cols
#             return 0 <= r < rows and 0 <= c < cols

#         rows, cols = len(heights), len(heights[0])

#         visited_pacific = set()
#         visited_atlantic = set()

#         def bfs(r, c, is_pacific):
#             queue = deque()
#             queue.append((r, c))
#             visited = visited_pacific if is_pacific else visited_atlantic
#             visited.add((r, c))
#             while queue:
#                 r, c = queue.popleft()
#                 for nr, nc in get_neighbours(r, c):
#                     if is_valid(nr, nc) and (nr, nc) not in visited \
#                         and heights[r][c] <= heights[nr][nc]:
#                         visited.add((nr, nc))
#                         queue.append((nr, nc))

#         # pacific
#         for r in range(rows):
#             for c in range(cols):
#                 if r == 0 or c == 0:
#                     bfs(r, c, True)

#         # atlantic
#         for r in reversed(range(rows)):
#             for c in reversed(range(cols)):
#                 if r == rows - 1 or c == cols - 1:
#                     bfs(r, c, False)

#         return list(map(list, visited_pacific & visited_atlantic))

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                for nr, nc in get_neighbours(r, c):
                    if is_valid(nr, nc) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        rows, cols = len(heights), len(heights[0])

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        return list(pacific_reachable & atlantic_reachable)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited = set()
        atlantic_visited = set()
        m = len(heights)
        n = len(heights[0])

        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c, is_pacific):
            visited = pacific_visited if is_pacific else atlantic_visited
            visited.add((r, c))
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and (nr, nc) not in visited \
                    and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, is_pacific)

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    if (r, c) not in pacific_visited:
                        dfs(r, c, True)
                if r == m - 1 or c == n - 1:
                    if (r, c) not in atlantic_visited:
                        dfs(r, c, False)

        return list(pacific_visited.intersection(atlantic_visited))

# leetcode submit region end(Prohibit modification and deletion)
