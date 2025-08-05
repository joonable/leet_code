# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the 
# intervals non-overlapping. 
# 
#  Note that intervals which only touch at a point are non-overlapping. For 
# example, [1, 2] and [2, 3] are non-overlapping. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-
# overlapping.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals 
# non-overlapping.
#  
# 
#  Example 3: 
# 
#  
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're 
# already non-overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10⁵ 
#  intervals[i].length == 2 
#  -5 * 10⁴ <= starti < endi <= 5 * 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming Greedy Sorting 👍 8547 👎 233

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            if prev_end <= interval[0]:
                prev_end = interval[1]
            else:
                result += 1
        return result


    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # non-overlapping 구간을 최대한 많이 유지하는 쪽으로 greedy하게 접근하는 게 최적
        # 끝나는 시간을 기준으로 정렬하면, 가장 빨리 끝나는 구간을 먼저 선택해서 다음 가능한 구간을 고를 수 있음 (Greedy)
        intervals.sort(key=lambda x: x[1])  # important
        prev_end = intervals[0][1]
        non_overlapping = 1 # important
        for start, end in intervals[1:]:
            if prev_end <= start:   # important
                prev_end = end
                non_overlapping += 1
        return len(intervals) - non_overlapping

# leetcode submit region end(Prohibit modification and deletion)
