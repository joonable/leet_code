# Given an m x n binary matrix filled with 0's and 1's, find the largest square 
# containing only 1's and return its area. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1",
# "1"],["1","0","0","1","0"]]
# Output: 4
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [["0"]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] is '0' or '1'. 
#  
# 
#  Related Topics Array Dynamic Programming Matrix 👍 10821 👎 253


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        answer = 0
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c])
                if matrix[r][c]:
                    answer = 1

        if not answer:
            return 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] and matrix[r - 1][c] and matrix[r][c - 1] \
                        and matrix[r - 1][c - 1]:
                    matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1],
                                       matrix[r - 1][c - 1]) + 1
                    answer = max(matrix[r][c], answer)
        return answer ** 2
        
# leetcode submit region end(Prohibit modification and deletion)
