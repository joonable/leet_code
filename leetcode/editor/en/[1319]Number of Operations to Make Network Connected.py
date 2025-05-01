# There are n computers numbered from 0 to n - 1 connected by ethernet cables 
# connections forming a network where connections[i] = [ai, bi] represents a 
# connection between computers ai and bi. Any computer can reach any other computer 
# directly or indirectly through the network. 
# 
#  You are given an initial computer network connections. You can extract 
# certain cables between two directly connected computers, and place them between any 
# pair of disconnected computers to make them directly connected. 
# 
#  Return the minimum number of times you need to do this in order to make all 
# the computers connected. If it is not possible, return -1. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between 
# computers 1 and 3.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁵ 
#  1 <= connections.length <= min(n * (n - 1) / 2, 10⁵) 
#  connections[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  There are no repeated connections. 
#  No two computers are connected by more than one cable. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 52
# 71 👎 80


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1  # important

    def get_component_count(self):
        return self.count


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:  # important
            return -1

        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)

        return uf.get_component_count() - 1

    def connected_components_323(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        return uf.get_component_count()

# leetcode submit region end(Prohibit modification and deletion)
