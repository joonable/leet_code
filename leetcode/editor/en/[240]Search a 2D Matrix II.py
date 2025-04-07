# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted in ascending from left to right. 
#  Integers in each column are sorted in ascending from top to bottom. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 5
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 20
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -10⁹ <= matrix[i][j] <= 10⁹ 
#  All the integers in each row are sorted in ascending order. 
#  All the integers in each column are sorted in ascending order. 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics Array Binary Search Divide and Conquer Matrix 👍 12389 👎 216


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if rows * cols == 1:
            return target == matrix[0][0]

        row_idx, col_idx = 0, cols - 1
        while row_idx <= rows - 1 and col_idx >= 0:
            val = matrix[row_idx][col_idx]
            if target == val:
                return True
            elif target < val:
                col_idx -= 1
            else:
                row_idx += 1
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
