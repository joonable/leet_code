# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 19000 👎 735


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # index를 저장
        result = []

        for i, num in enumerate(nums):
            # 1. 윈도우 범위를 벗어난 index 제거
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. 새로운 값보다 작은 값들은 뒤에서 제거
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 3. 현재 index 추가
            dq.append(i)

            # 4. 윈도우 시작되면 최대값 추가
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
# leetcode submit region end(Prohibit modification and deletion)
