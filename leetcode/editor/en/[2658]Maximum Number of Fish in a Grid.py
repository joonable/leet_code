# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) 
# represents: 
# 
#  
#  A land cell if grid[r][c] = 0, or 
#  A water cell containing grid[r][c] fish, if grid[r][c] > 0. 
#  
# 
#  A fisher can start at any water cell (r, c) and can do the following 
# operations any number of times: 
# 
#  
#  Catch all the fish at cell (r, c), or 
#  Move to any adjacent water cell. 
#  
# 
#  Return the maximum number of fish the fisher can catch if he chooses his 
# starting cell optimally, or 0 if no water cell exists. 
# 
#  An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 
# 1), (r + 1, c) or (r - 1, c) if it exists. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move 
# to cell (2,3) and collect 4 fish.
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Output: 1
# Explanation: The fisher can start at cells (0,0) or (3,3) and collect a 
# single fish. 
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10 
#  0 <= grid[i][j] <= 10 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 939 👎 65


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_fish = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            result = grid[r][c]
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    result += dfs(nr, nc)
            return result

        max_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_fish = max(dfs(r, c), max_fish)
        return max_fish

# leetcode submit region end(Prohibit modification and deletion)
