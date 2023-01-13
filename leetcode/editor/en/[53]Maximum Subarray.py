# Given an integer array nums, find the subarray which has the largest sum and 
# return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
# 
#  Related Topics Array Divide and Conquer Dynamic Programming 👍 26931 👎 1205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #
    #     if len(nums) == 1: return nums[0]
    #     if all([x < 0 for x in nums]): return max(nums)
    #
    #     l_idx = 0
    #     for idx, num in enumerate(nums):
    #         if num < 0:
    #             if sum(nums[l_idx:idx+1]) < 0:
    #                 l_idx = idx+1
    #
    #     r_idx = 0
    #     list_reversed_nums = list(reversed(nums[l_idx:]))
    #     for idx, num in enumerate(list_reversed_nums):
    #         if num < 0:
    #             if sum(list_reversed_nums[r_idx:idx+1]) < 0:
    #                 r_idx = idx+1
    #
    #     r_idx = len(nums) - r_idx
    #     # print(nums, nums[l_idx:r_idx], l_idx, r_idx)
    #     return sum(nums[l_idx:r_idx])

    # def maxSubArray(self, nums: List[int]) -> int:
    #
    #     if len(nums) == 1: return nums[0]
    #     if all([x < 0 for x in nums]): return max(nums)
    #
    #     len_nums = len(nums)
    #     left_idx = 0
    #     right_idx = len_nums - 1
    #
    #     for idx in range(len_nums):
    #         tmp_left_idx = idx
    #         tmp_right_idx = len_nums - idx - 1
    #
    #         if tmp_left_idx > tmp_right_idx: break
    #
    #         if nums[tmp_left_idx] < 0:
    #             if sum(nums[left_idx:tmp_left_idx+1]) < 0:
    #                 left_idx = tmp_left_idx+1
    #
    #         if nums[tmp_right_idx] < 0:
    #             if sum(nums[tmp_right_idx:right_idx+1]) < 0:
    #                 right_idx = tmp_right_idx-1
    #
    #         right_idx = right_idx if right_idx != -1 else len_nums - 1
    #
    #     print(nums, nums[left_idx:right_idx+1], left_idx, right_idx)
    #     return sum(nums[left_idx:right_idx+1])

    def maxSubArray(self, nums: List[int]) -> int:

        len_nums = len(nums)
        if all([x < 0 for x in nums]): return max(nums)

        if len_nums <= 2:
            if all([x > 0 for x in nums]):
                return sum(nums)
            else:
                return max(nums)

        left_idx = 0
        right_idx = len_nums - 1
        list_nums = nums.copy()

        while(True):
            list_two_nums = [list_nums[i] + list_nums[i + 1] for i in range(len(list_nums) - 1)]
            if all(map(lambda x: x > 0, list_two_nums)): break

            for two_num in list_two_nums:
                if two_num < 0:
                    left_idx+=1
                else:
                    if nums[left_idx] < 0:
                        left_idx += 1
                    break

            for two_num in reversed(list_two_nums):
                if two_num < 0:
                    right_idx -= 1
                else:
                    if nums[right_idx+1] < 0:
                        right_idx -= 1
                    break
            list_nums = list_two_nums.copy()

        print(nums, nums[left_idx:right_idx+1], left_idx, right_idx)
        return sum(nums[left_idx:right_idx+1])