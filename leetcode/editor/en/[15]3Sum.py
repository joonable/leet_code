# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not 
# matter.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Two Pointers Sorting 👍 32590 👎 3068


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if nums[i] > 0: # important
                break
            if i > 0 and nums[i - 1] == nums[i]:    # important
                continue

            left, right = i + 1, n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1       # important

                    # important
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # important
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
# leetcode submit region end(Prohibit modification and deletion)
