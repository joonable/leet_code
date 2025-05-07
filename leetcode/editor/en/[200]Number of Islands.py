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


    def numDistinctIslands_bfs_261(self, grid: List[List[int]]) -> int:
        # Problem
        # input: grid: List[List[int]] -> 0 = water, 1 = island
        # output: n_distinct_islands in their shape
        # island - one island can be translated (moved up/down/left/right)
        # shape -rotation, reflection -> different islands

        # Approach: bfs + set(based on relative position)
        # result = set()
        # for loop grid:
        #   if 1 found -> add neighbours in the queue if the position is valid.
        #   neighbours: left(-1, 0), right: (0, +1)...
        #   temp = list(), append visited places based on the starting point.
        #   queue empty -> result.add(temp)
        # valid position: no index error, not visited
        # visited: 1 -> 0 not to visit already visited places

        n_rows = len(grid)
        n_cols = len(grid[0])

        queue = deque([])
        result = set()

        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < n_rows and 0 <= c < n_cols and grid[r][c] == 1



        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                    path = [(0, 0)]
                    while queue:
                        r, c = queue.popleft()
                          # visited
                        for nr, nc in get_neighbours(r, c):
                            if is_valid(nr, nc):
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                                path.append((nr - i, nc - j))
                    result.add(tuple(path))

        return len(result)


    def numDistinctIslands_dfs_694(self, grid: List[List[int]]) -> int:
        # Problem
        # input: grid: List[List[int]] -> 0 = water, 1 = island
        # output: n_distinct_islands in their shape
        # island - one island can be translated (moved up/down/left/right)
        # shape -rotation, reflection -> different islands

        n_rows = len(grid)
        n_cols = len(grid[0])
        result = set()

        neighbours = {
            "L": (-1, 0),
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1)
        }

        def is_valid(r, c):
            return 0 <= r < n_rows and 0 <= c < n_cols and grid[r][c] == 1

        def dfs(r, c, d):   # important
            grid[r][c] = 0
            path.append(d)
            for d, (dr, dc) in neighbours.items():
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    dfs(nr, nc, d)

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    path = []
                    dfs(r, c, 'O')  # important
                    result.add(tuple(path)) # important

        return len(result)


from collections import deque
def wall_and_gate_286(grid):
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

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
    return grid




# leetcode submit region end(Prohibit modification and deletion)
