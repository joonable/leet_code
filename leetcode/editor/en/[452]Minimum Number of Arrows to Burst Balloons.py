# There are some spherical balloons taped onto a flat wall that represents the 
# XY-plane. The balloons are represented as a 2D integer array points where points[
# i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches 
# between xstart and xend. You do not know the exact y-coordinates of the balloons. 
# 
#  Arrows can be shot up directly vertically (in the positive y-direction) from 
# different points along the x-axis. A balloon with xstart and xend is burst by 
# an arrow shot at x if xstart <= x <= xend. There is no limit to the number of 
# arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any 
# balloons in its path. 
# 
#  Given the array points, return the minimum number of arrows that must be 
# shot to burst all balloons. 
# 
#  
#  Example 1: 
# 
#  
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
#  
# 
#  Example 2: 
# 
#  
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 
# arrows.
#  
# 
#  Example 3: 
# 
#  
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= points.length <= 10⁵ 
#  points[i].length == 2 
#  -2³¹ <= xstart < xend <= 2³¹ - 1 
#  
# 
#  Related Topics Array Greedy Sorting 👍 7760 👎 259


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 가장 먼저 끝나는 풍선부터 고려하면서, 화살의 최적 위치를 그 풍선의 끝 지점에 쏘면,
        # 그 위치와 겹치는 모든 풍선을 한꺼번에 제거할 수 있음.
        # x[0]반례 = [[1,10], [2,3], [4,5], [6,7]]
        points.sort(key=lambda x: x[1])     # important
        prev_arrow_pos = -float('inf')
        n_arrow = 0
        for start, end in points:
            if start > prev_arrow_pos:
                n_arrow += 1
                prev_arrow_pos = end
        return n_arrow
# leetcode submit region end(Prohibit modification and deletion)
