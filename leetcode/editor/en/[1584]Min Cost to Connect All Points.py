# You are given an array points representing integer coordinates of some points 
# on a 2D-plane, where points[i] = [xi, yi]. 
# 
#  The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute 
# value of val. 
# 
#  Return the minimum cost to make all points connected. All points are 
# connected if there is exactly one simple path between any two points. 
# 
#  
#  Example 1: 
#  
#  
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
#  
# 
#  Example 2: 
# 
#  
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= points.length <= 1000 
#  -10⁶ <= xi, yi <= 10⁶ 
#  All pairs (xi, yi) are distinct. 
#  
# 
#  Related Topics Array Union Find Graph Minimum Spanning Tree 👍 5303 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappush, heappop, heapify

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


class Solution:


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        # time - O(n**2)
        for i in range(n):
            u = points[i]
            for j in range(i + 1, n):
                v = points[j]
                cost = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append([cost, i, j])

        # time - O(n**2 * logn), space - O(n**2)
        edges.sort(key=lambda x: x[0])  # important

        total_cost = 0
        uf = UnionFind(n)
        # time - O(n**2)
        for cost, i, j in edges:
            if uf.union(i, j):  # avoid cycle!
                total_cost += cost

        return total_cost


    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]      # (비용, 정점 번호) — 시작은 비용 0, 노드 0
        total_cost = 0

        while len(visited) < n:
            cost, u = heappop(heap)     # 최소 비용 간선 선택 (Greedy)
            if u in visited:
                continue
            total_cost += cost
            visited.add(u)

            # u와 연결 가능한 모든 노드(v)에 대해
            for v in range(n):
                if v not in visited:
                    # u–v 간의 맨해튼 거리 계산
                    new_cost = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heappush(heap, (new_cost, v))
        return total_cost


    def connecting_cities_with_minimum_cost_1135(self, n, connections):
        if len(connections) < n - 1:
            return -1

        total_cost = 0
        uf = UnionFind(n + 1)  # 1-index
        connections.sort(key=lambda x: x[2])    # time = O(n^2 * log n), space = O(n^2)

        # time = O(n^2)
        for i, j, cost in connections:
            if uf.union(i, j):  # avoid cycle
                total_cost += cost

        roots = set(uf.find(i) for i in range(1, n + 1))
        return total_cost if len(roots) == 1 else -1


        
# leetcode submit region end(Prohibit modification and deletion)
