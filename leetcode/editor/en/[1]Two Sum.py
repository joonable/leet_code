# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than 
# O(n²)
#  time complexity?
# 
#  Related Topics Array Hash Table 👍 53162 👎 1753


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     """
    #     Success:
    #         Runtime:2364 ms, faster than 33.31% of Python3 online submissions.
    #         Memory Usage:17.1 MB, less than 79.34% of Python3 online submissions.
    #     """
    #
    #     for i in range(len(nums)):
    #         n1 = nums[i]
    #         for j in range(i+1, len(nums)):
    #             n2 = nums[j]
    #             if n1 + n2 < target:
    #                 continue
    #             elif n1 + n2 == target:
    #                 return [i, j]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Success:
            Runtime:61 ms, faster than 81.09% of Python3 online submissions.
            Memory Usage:17.4 MB, less than 57.94% of Python3 online submissions.
        """

        dict_seen = {}
        for i in range(len(nums)):
            n = nums[i]
            true_n = target - n
            if dict_seen.get(true_n, -1) == -1:
                dict_seen[n] = i
            else:
                return [dict_seen[true_n], i]


    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     dict_nums = {v: idx for idx, v in enumerate(nums)}
    #     for i, v in enumerate(nums):
    #         diff = target - v
    #         if diff in dict_nums:
    #             j = dict_nums[diff]
    #             if i != j:
    #                 return sorted([i, j])