# In a gold mine grid of size m x n, each cell in this mine has an integer 
# representing the amount of gold in that cell, 0 if it is empty. 
# 
#  Return the maximum amount of gold you can collect under the conditions: 
# 
#  
#  Every time you are located in a cell you will collect all the gold in that 
# cell. 
#  From your position, you can walk one step to the left, right, up, or down. 
#  You can't visit the same cell more than once. 
#  Never visit a cell with 0 gold. 
#  You can start and stop collecting gold from any position in the grid that 
# has some gold. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 15 
#  0 <= grid[i][j] <= 100 
#  There are at most 25 cells containing gold. 
#  
# 
#  Related Topics Array Backtracking Matrix 👍 3414 👎 104


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs_v1(r, c, visited):
            visited.add((r, c))
            golds = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] and not (nr, nc) in visited:
                        golds.append(dfs(nr, nc))
            visited.remove()
            return grid[r][c] + (max(golds) if golds else 0)

        def dfs_v2(r, c):
            gold, grid[r][c] = grid[r][c], 0
            golds = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    golds.append(dfs_v2(nr, nc))
            grid[r][c] = gold
            return grid[r][c] + (max(golds) if golds else 0)

        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_gold = max(dfs_v2(r, c), max_gold)
        return max_gold
# leetcode submit region end(Prohibit modification and deletion)
