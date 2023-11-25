# You are given an n x n 2D matrix representing an image, rotate the image by 90
#  degrees (clockwise). 
# 
#  You have to rotate the image in-place, which means you have to modify the 
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == matrix.length == matrix[i].length 
#  1 <= n <= 20 
#  -1000 <= matrix[i][j] <= 1000 
#  
# 
#  Related Topics Array Math Matrix 👍 16550 👎 730


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Success:
            Runtime:35 ms, faster than 91.71% of Python3 online submissions.
            Memory Usage:16.5 MB, less than 22.67% of Python3 online submissions.
        """
        n = len(matrix)
        temp_matrix = [l.copy() for l in matrix]
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = temp_matrix[i][j]


# leetcode submit region end(Prohibit modification and deletion)
