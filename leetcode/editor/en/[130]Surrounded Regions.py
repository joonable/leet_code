# You are given an m x n matrix board containing letters 'X' and 'O', capture 
# regions that are surrounded: 
# 
#  
#  Connect: A cell is connected to adjacent cells horizontally or vertically. 
#  Region: To form a region connect every 'O' cell. 
#  Surround: The region is surrounded with 'X' cells if you can connect the 
# region with 'X' cells and none of the region cells are on the edge of the board. 
#  
# 
#  To capture a surrounded region, replace all 'O's with 'X's in-place within 
# the original board. You do not need to return anything. 
# 
#  
#  Example 1: 
# 
#  
#  Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X",
# "O","X","X"]] 
#  
# 
#  Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X",
# "X"]] 
# 
#  Explanation: 
#  
#  In the above diagram, the bottom region is not captured because it is on the 
# edge of the board and cannot be surrounded. 
# 
#  Example 2: 
# 
#  
#  Input: board = [["X"]] 
#  
# 
#  Output: [["X"]] 
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] is 'X' or 'O'. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 9135 👎 2048


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_neighbours(r, c):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

        def is_valid(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            for nr, nc in get_neighbours(r, c):
                if is_valid(nr, nc) and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    dfs(nr, nc)

        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    board[r][c] = '#'
                    dfs(r, c)

        convert = {'O': 'X', 'X': 'X', '#': 'O'}
        for r in range(0, rows):
            for c in range(0, cols):
                board[r][c] = convert[board[r][c]]

# leetcode submit region end(Prohibit modification and deletion)
