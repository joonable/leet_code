# Given an m x n matrix, return all elements of the matrix in spiral order. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics Array Matrix Simulation 👍 15529 👎 1396


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        total_visited_cnt = n_cols * n_rows

        idx_direction = 0
        list_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        ptr_i = 0
        ptr_j = 0

        result = [matrix[0][0]]
        visited = [[False] * n_cols for _ in range(n_rows)]
        visited[0][0] = True
        visited_cnt = 1

        while True:
            # print(result)
            if visited_cnt == total_visited_cnt:
                break

            direction = list_direction[idx_direction]
            if ptr_i + direction[0] == n_rows or ptr_j + direction[1] == n_cols \
                    or ptr_i + direction[0] < 0 or ptr_j + direction[1] < 0:
                idx_direction = (idx_direction + 1) % 4
                continue
            elif visited[ptr_i + direction[0]][ptr_j + direction[1]]:
                idx_direction = (idx_direction + 1) % 4
                continue
            else:
                ptr_i += direction[0]
                ptr_j += direction[1]
                result.append(matrix[ptr_i][ptr_j])
                visited[ptr_i][ptr_j] = True
                visited_cnt += 1

        return result

        
# leetcode submit region end(Prohibit modification and deletion)
