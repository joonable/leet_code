from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # Inserts a new interval into a list of non-overlapping intervals and merges if necessary
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        # Iterate through all existing intervals
        for interval in intervals:
            # If the current interval ends before the new interval starts, there's no overlap
            if interval[1] < newInterval[0]:
                merged.append(interval)
            # If the current interval starts after the new interval ends, no overlap and newInterval should be added
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval
            # Overlapping intervals, merge them by updating the newInterval boundaries
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        # Add the last interval (merged or standalone) to the result list
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
