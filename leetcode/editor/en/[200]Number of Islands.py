# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 23648 👎 559


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     island_cnt = 0

    #     def get_neighbours(r, c):
    #         return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

    #     def is_valid(r, c):
    #         return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    #     def bfs(r, c):
    #         queue = deque([(r, c)])
    #         while queue:
    #             r, c = queue.popleft()
    #             for nr, nc in get_neighbours(r, c):
    #                 if is_valid(nr, nc) and grid[nr][nc] == '1':
    #                     grid[nr][nc] = '0'
    #                     queue.append((nr, nc))

    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if grid[r][c] == '1':
    #                 grid[r][c] = '0'
    #                 island_cnt += 1
    #                 bfs(r, c)
    #     return island_cnt

    def numIslands(self, grid: List[List[str]]) -> int:
        island_cnt = 0

        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            grid[r][c] = '0'
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    island_cnt += 1
                    dfs(r, c)

        return island_cnt

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        def dfs(r, c, dir_letter):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                path.append(dir_letter)
                for d, (dr, dc) in directions.items():
                    dfs(r + dr, c + dc, d)

        rows, cols = len(grid), len(grid[0])
        unique_shapes = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    path = []
                    dfs(r, c, 'O')  # 'O' for origin
                    unique_shapes.add(tuple(path))

        return len(unique_shapes)

from collections import deque
def wall_and_gate_238(grid):
    rows, cols = len(grid), len(grid[0])
    INF = 2 ** 31 - 1

    def get_neighbours(r, c):
        return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

    def is_valid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                queue.append((r, c))

    level = 0
    while queue:
        level += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and grid[nr][nc] == INF:
                    grid[nr][nc] = level
                    queue.append((nr, nc))
    return grid




# leetcode submit region end(Prohibit modification and deletion)
