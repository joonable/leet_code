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
#  Return the ordering of courses you should take to finish all courses. If 
# there are many valid answers, return any of them. If it is impossible to finish all 
# courses, return an empty array. 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you 
# should have finished course 0. So the correct course order is [0,1].
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you 
# should have finished both courses 1 and 2. Both courses 1 and 2 should be taken 
# after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3
# ].
#  
# 
#  Example 3: 
# 
#  
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= numCourses * (numCourses - 1) 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  ai != bi 
#  All the pairs [ai, bi] are distinct. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Graph Topological 
# Sort 👍 11275 👎 362


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        모든 노드를 방문했다면 = numCourses == 0
        → 이는 사이클 없이 모든 노드를 위상정렬한 것과 동일한 의미!
        '''
        in_degrees = [0] * numCourses
        next_courses = defaultdict(list)

        for next_course, prev_course in prerequisites:
            in_degrees[next_course] += 1
            next_courses[prev_course].append(next_course)

        queue = deque()
        result = []

        for course, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                queue.append(course)

        while queue:
            prev_course = queue.popleft()
            result.append(prev_course)
            numCourses -= 1
            for next_course in next_courses[prev_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return result if numCourses == 0 else []

from collections import defaultdict
def alien_dictionary_269(words):
    next_chars = defaultdict(set)
    in_degrees = dict()

    # Step 1: 모든 문자 in_degrees에 등록
    for word in words:
        for ch in word:
            in_degrees[ch] = 0  # important

    # Step 2: 단어들 쌍 비교해서 그래프(edge) 만들기
    for i in range(len(words) - 1):
        prev_word = words[i]
        next_word = words[i + 1]
        if len(prev_word) >= len(next_word) \
                and prev_word.startswith(next_word):
            return ""

        for p_ch, n_ch in zip(prev_word, next_word):
            if p_ch != n_ch:     # important
                if n_ch not in next_chars[p_ch]:    # important
                    next_chars[p_ch].add(n_ch)
                    in_degrees[n_ch] += 1
                break

    # Step 3: Topological Sort
    queue = deque([ch for ch, degree in in_degrees.items() if degree == 0])

    result = []
    while queue:
        p_ch = queue.popleft()
        result.append(p_ch)
        for n_ch in next_chars[p_ch]:
            in_degrees[n_ch] -= 1
            if in_degrees[n_ch] == 0:
                queue.append(n_ch)

    return "".join(result) if len(result) == len(in_degrees) else "" # important

# leetcode submit region end(Prohibit modification and deletion)
