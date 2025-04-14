# Given an m x n integer matrix matrix, if an element is 0, set its entire row 
# and column to 0's. 
# 
#  You must do it in place. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[0].length 
#  1 <= m, n <= 200 
#  -2³¹ <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  
#  Follow up: 
# 
#  
#  A straightforward solution using O(mn) space is probably a bad idea. 
#  A simple improvement uses O(m + n) space, but still not the best solution. 
#  Could you devise a constant space solution? 
#  
# 
#  Related Topics Array Hash Table Matrix 👍 15478 👎 787


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))   # important
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))   # important

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0


# leetcode submit region end(Prohibit modification and deletion)
