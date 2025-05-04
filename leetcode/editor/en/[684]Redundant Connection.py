# In this problem, a tree is an undirected graph that is connected and has no 
# cycles. 
# 
#  You are given a graph that started as a tree with n nodes labeled from 1 to 
# n, with one additional edge added. The added edge has two different vertices 
# chosen from 1 to n, and was not an edge that already existed. The graph is 
# represented as an array edges of length n where edges[i] = [ai, bi] indicates that there 
# is an edge between nodes ai and bi in the graph. 
# 
#  Return an edge that can be removed so that the resulting graph is a tree of 
# n nodes. If there are multiple answers, return the answer that occurs last in 
# the input. 
# 
#  
#  Example 1: 
#  
#  
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#  
# 
#  Example 2: 
#  
#  
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == edges.length 
#  3 <= n <= 1000 
#  edges[i].length == 2 
#  1 <= ai < bi <= edges.length 
#  ai != bi 
#  There are no repeated edges. 
#  The given graph is connected. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 68
# 58 👎 436


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # input: len(edges) = n
        # -> supposed to be n - 1 if it doesn't have a cycle in the graph
        # output: we need return the edge making a cycle
        # constraints: 1-index

        # UnionFind -> dectect a cycle
        # union(x, y) -> bool: if True (= already connected) x, y is the edge making a cycle

        uf = UnionFind(len(edges) + 1)  # 1-index
        for x, y in edges:
            if not uf.union(x, y):
                return [x, y]


# leetcode submit region end(Prohibit modification and deletion)
