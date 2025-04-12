# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem 
# constraint.
#  
# 
#  Example 2: 
# 
#  
# Input: target = 4, nums = [1,4,4]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  
# Follow up: If you have figured out the 
# O(n) solution, try coding another solution of which the time complexity is 
# O(n log(n)).
# 
#  Related Topics Array Binary Search Sliding Window Prefix Sum 👍 13094 👎 474


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        left = 0
        cur_sum = 0



        # We fix `right` by iterating with a for loop,
        for right in range(n): # important
            cur_sum += nums[right]

            # keep increasing `left` as long as it's less than or equal to `right` to find the minimum length.
            # Since we're looking for the minimum length, there's no need to revisit a `left` once it's moved forward.
            while left <= right and cur_sum >= target:  # important
                min_len = min(right - left + 1, min_len)
                cur_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


        # i, j = 0, 0
        # min_len = 0
        # while not i == j == len(nums)-1:
        #     sum_output = sum(nums[i:j+1])
        #     if sum_output == target:
        #         if min_len == 0 or min_len > j+1-i:
        #             min_len = j+1 - i
        #         i += 1
        #     elif i == j:
        #         j += 1
        #     elif j == len(nums)-1:
        #         i += 1
        #     elif sum_output < target:
        #         j += 1
        #     else:
        #         i += 1
        # return min_len
        
# leetcode submit region end(Prohibit modification and deletion)
