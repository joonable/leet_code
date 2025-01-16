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
        i, j = 0, 0
        min_len = 0
        while not i == j == len(nums)-1:
            sum_output = sum(nums[i:j+1])
            if sum_output == target:
                if min_len == 0 or min_len > j+1-i:
                    min_len = j+1 - i
                i += 1
            elif i == j:
                j += 1
            elif j == len(nums)-1:
                i += 1
            elif sum_output < target:
                j += 1
            else:
                i += 1
        return min_len
        
# leetcode submit region end(Prohibit modification and deletion)
