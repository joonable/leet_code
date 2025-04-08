# Given an array of intervals where intervals[i] = [starti, endi], merge all 
# overlapping intervals, and return an array of the non-overlapping intervals that 
# cover all the intervals in the input. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics Array Sorting 👍 22824 👎 829


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
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
