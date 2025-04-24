# There are n cities. Some of them are connected, while some are not. If city a 
# is connected directly with city b, and city b is connected directly with city c,
#  then city a is connected indirectly with city c. 
# 
#  A province is a group of directly or indirectly connected cities and no 
# other cities outside of the group. 
# 
#  You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the 
# iᵗʰ city and the jᵗʰ city are directly connected, and isConnected[i][j] = 0 
# otherwise. 
# 
#  Return the total number of provinces. 
# 
#  
#  Example 1: 
#  
#  
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#  
# 
#  Example 2: 
#  
#  
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 200 
#  n == isConnected.length 
#  n == isConnected[i].length 
#  isConnected[i][j] is 1 or 0. 
#  isConnected[i][i] == 1 
#  isConnected[i][j] == isConnected[j][i] 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 10
# 338 👎 387


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # important - path compression
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:    # important
                parent[root_x] = parent[root_y]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return len(set(find(i) for i in range(n)))  # important

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         visited = [False] * n
#
#         def dfs(node):
#             for neighbor in range(n):
#                 if isConnected[node][neighbor] == 1 and not visited[neighbor]:
#                     visited[neighbor] = True
#                     dfs(neighbor)
#
#         province_count = 0
#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = True
#                 dfs(i)
#                 province_count += 1
#
#         return province_count
        
# leetcode submit region end(Prohibit modification and deletion)
