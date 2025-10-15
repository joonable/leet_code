# Given a m x n grid filled with non-negative numbers, find a path from top 
# left to bottom right, which minimizes the sum of all numbers along its path. 
# 
#  Note: You can only move either down or right at any point in time. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 200 
#  
# 
#  Related Topics Array Dynamic Programming Matrix 👍 12827 👎 178
from itertools import accumulate

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum_inf(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_val = float("inf")
        for r in range(rows):
            for c in range(cols):
                if r == c == 0:
                    continue
                left = grid[r][c - 1] if c != 0 else max_val
                top = grid[r - 1][c] if r != 0 else max_val
                grid[r][c] += min(left, top)
        return grid[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]

        for c in range(1, cols):
            grid[0][c] += grid[0][c - 1]

        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
