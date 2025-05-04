# You are given an array of variable pairs equations and an array of real 
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai 
# / Bi = values[i]. Each Ai or Bi is a string that represents a single variable. 
# 
#  You are also given some queries, where queries[j] = [Cj, Dj] represents the 
# jᵗʰ query where you must find the answer for Cj / Dj = ?. 
# 
#  Return the answers to all queries. If a single answer cannot be determined, 
# return -1.0. 
# 
#  Note: The input is always valid. You may assume that evaluating the queries 
# will not result in division by zero and that there is no contradiction. 
# 
#  Note: The variables that do not occur in the list of equations are undefined,
#  so the answer cannot be determined for them. 
# 
#  
#  Example 1: 
# 
#  
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a",
# "c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0 
# 
#  Example 2: 
# 
#  
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#  
# 
#  Example 3: 
# 
#  
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"]
# ,["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= Ai.length, Bi.length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= Cj.length, Dj.length <= 5 
#  Ai, Bi, Cj, Dj consist of lower case English letters and digits. 
#  
# 
#  Related Topics Array String Depth-First Search Breadth-First Search Union 
# Find Graph Shortest Path 👍 9717 👎 1022
from Cython import union


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.parent = {}  # parent[x] = the root of x
        self.weight = {}  # weight[x] = x / parent[x]

    def find(self, x):
        # Initialize unseen node
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
            return x

        # Path compression with weight update
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(orig_parent)
            self.weight[x] *= self.weight[orig_parent]  # Maintain ratio to new root

        return self.parent[x]

    def union(self, x, y, value):
        """
        Given x / y = value, we need to connect x and y.
        Suppose:
          - weight[x] = x / root_x
          - weight[y] = y / root_y
        Then to make x / y = value, we solve for:
          root_x / root_y = value * (weight[y] / weight[x])
        So we connect root_x to root_y and update the weight.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = value * self.weight[y] / self.weight[x]

    def calculate_query(self, x, y):
        """
        To compute x / y:
        - Check if both are in the graph
        - If they are connected (same root), return weight[x] / weight[y]
        - Otherwise, return -1.0
        """
        if x not in self.parent or y not in self.parent:
            return -1.0

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            return -1.0

        return self.weight[x] / self.weight[y]


class Solution:
    from typing import List
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the union-find graph with weighted connections
        uf = UnionFind()
        for (x, y), val in zip(equations, values):
            uf.union(x, y, val)

        # Process each query using the constructed structure
        return [uf.calculate_query(x, y) for x, y in queries]

class Solution_277:
    def get_celebrity(self, n: int) -> int:
        def knows(x, y) -> bool:
            ...

        celebrity = 0
        for candidate in range(1, n):
            if knows(celebrity, candidate):
                celebrity = candidate

        for candidate in range(n):
            if candidate == celebrity:
                continue
            # if knows(celebrity, candidate) or not knows(candidate, celebrity):
            #     return -1
            if knows(candidate, celebrity) and not knows(celebrity, candidate):
                continue
            return -1
        return celebrity



""" 261 Graph Valid Tree 프리미엄
You have a graph of n nodes labeled from 0 to n - 1 and a list of edges, where each edge is a pair of nodes.
Return true if the edges form a valid tree, and false otherwise.
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.n_roots = n    # important

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y: # no cycle
            self.parent[root_x] = root_y
            self.n_roots -= 1       # important
            return True
        return False


class Solution_261:
    from typing import List
    # Problem
    # input: edges: List[List[int]] e.g. [0, n - 1] -> a pair of nodes
    # output: bool ->
    # if the given graph is a valid tree,
    # there should be no cycle in the graph
    #   and all nodes are connected

    # important constraints: len(edges) == n - 1
    #
    # Approach -> UnionFind (undirected + detect cycle + connected components)
    # union + for loop -> detect a cycle while union -> return False
    # after union -> if there are more than one root -> disconnected components -> return False

    def is_valid_tree(self, edges: List[List[int]]) -> bool:
        nodes = set()
        for x, y in edges:
            nodes.add(x)
            nodes.add(y)
        n = len(nodes)

        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y): # if union fails -> there is a cycle
                return False

        # roots = set(uf.find(i) for i in range(n))
        return uf.n_roots == 1 # important


# leetcode submit region end(Prohibit modification and deletion)
