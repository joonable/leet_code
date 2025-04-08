# You are given an array of non-overlapping intervals intervals where intervals[
# i] = [starti, endi] represent the start and the end of the iᵗʰ interval and 
# intervals is sorted in ascending order by starti. You are also given an interval 
# newInterval = [start, end] that represents the start and end of another interval. 
# 
#  Insert newInterval into intervals such that intervals is still sorted in 
# ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary). 
# 
#  Return intervals after the insertion. 
# 
#  Note that you don't need to modify intervals in-place. You can make a new 
# array and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁵ 
#  intervals is sorted by starti in ascending order. 
#  newInterval.length == 2 
#  0 <= start <= end <= 10⁵ 
#  
# 
#  Related Topics Array 👍 10803 👎 859

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])
        # result = [intervals[0]]
        #
        # for interval in intervals[1:]:
        #     if result[-1][1] >= interval[0]:
        #         result[-1][1] = max(result[-1][1], interval[1])
        #     else:
        #         result.append(interval)
        #
        # return result

        merged = []
        i = 0
        n = len(intervals)

        # Step 1: add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Step 2: merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Step 3: add the merged newInterval
        merged.append(newInterval)

        # Step 4: add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
# leetcode submit region end(Prohibit modification and deletion)
