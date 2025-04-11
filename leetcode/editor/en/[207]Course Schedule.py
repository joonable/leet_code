# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai,
#  bi] indicates that you must take course bi first if you want to take course ai.
#  
# 
#  
#  For example, the pair [0, 1], indicates that to take course 0 you have to 
# first take course 1. 
#  
# 
#  Return true if you can finish all courses. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you 
# should also have finished course 1. So it is impossible.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= 5000 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  All the pairs prerequisites[i] are unique. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Graph Topological 
# Sort 👍 16947 👎 795


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        graph = defaultdict(list)
        for prev_course, next_course in prerequisites:
            in_degrees[next_course] += 1
            graph[prev_course].append(next_course)

        q = deque()
        for course, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(course)

        completed_course = 0
        while q:
            course = q.popleft()
            completed_course += 1

            for next_course in graph[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    q.append(next_course)

        return completed_course == numCourses

        # # dfs
        # graph = defaultdict(list)
        # for a, b in prerequisites:
        #     graph[b].append(a)
        #
        # visited = [0] * numCourses  # 0 = unvisited, -1 = visiting, 1 = visited
        #
        # def dfs(course):
        #     if visited[course] == -1:  # 현재 경로에서 다시 만남 → 사이클
        #         return False
        #     if visited[course] == 1:  # 이미 확인된 노드 → OK
        #         return True
        #
        #     visited[course] = -1  # 방문 시작
        #     for neighbor in graph[course]:
        #         if not dfs(neighbor):
        #             return False
        #     visited[course] = 1  # 방문 완료
        #     return True
        #
        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False
        # return True

# leetcode submit region end(Prohibit modification and deletion)
