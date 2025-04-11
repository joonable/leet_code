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
        merged = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged.append(newInterval)
        return merged

def meeting_rooms_252(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False
    return True

def meeting_rooms_253(intervals: List[List[int]]) -> int:
    starts = []
    ends = []
    for interval in intervals:
        starts.append(interval[0])
        ends.append(interval[1])

    starts.sort()
    ends.sort()

    start_idx = 0
    end_idx = 0

    k = 0
    max_k = k
    while start_idx < len(intervals):
        if starts[start_idx] < ends[end_idx]:
            start_idx += 1
            k += 1
            max_k = max(max_k, k)
        else:
            end_idx += 1
            k -= 1
    return max_k
# leetcode submit region end(Prohibit modification and deletion)
