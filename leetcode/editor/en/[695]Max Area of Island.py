# You are given an m x n binary matrix grid. An island is a group of 1's (
# representing land) connected 4-directionally (horizontal or vertical.) You may assume 
# all four edges of the grid are surrounded by water. 
# 
#  The area of an island is the number of cells with a value 1 in the island. 
# 
#  Return the maximum area of an island in grid. If there is no island, return 0
# . 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,
# 0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,
# 0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-
# directionally.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 10252 👎 213


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            grid[r][c] = 0
            cur_area = 1
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and grid[nr][nc]:
                    cur_area += dfs(nr, nc)
            return cur_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_area = max(max_area, dfs(r, c))

        return max_area
# leetcode submit region end(Prohibit modification and deletion)
