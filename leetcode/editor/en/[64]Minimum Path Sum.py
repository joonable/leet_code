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
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return sum(grid[0])
        max_val = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                    continue
                prev_i = grid[i-1][j] if i != 0 else max_val
                prev_j = grid[i][j-1] if j != 0 else max_val
                grid[i][j] = grid[i][j] + min(prev_i, prev_j)
        return grid[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
