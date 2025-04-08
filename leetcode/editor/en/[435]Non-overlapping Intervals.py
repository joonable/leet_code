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
        intervals.sort(key=lambda x: x[1])

        non_overlap_count = 1
        prev_interval = intervals[0]

        for interval in intervals[1:]:
            if prev_interval[1] > interval[0]:
                continue

            prev_interval = interval
            non_overlap_count += 1

        return len(intervals) - non_overlap_count
# leetcode submit region end(Prohibit modification and deletion)
