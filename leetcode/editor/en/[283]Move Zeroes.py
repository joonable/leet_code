# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done?
# 
#  Related Topics Array Two Pointers 👍 15645 👎 399


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def moveZeroes(self, nums: list[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     Success:
    #         Runtime:138 ms, faster than 86.81% of Python3 online submissions.
    #         Memory Usage:18 MB, less than 15.97% of Python3 online submissions.
    #     """
    #     list_non_zero = [n for n in nums if n != 0]
    #     cnt_zero = len(nums) - len(list_non_zero)
    #     if cnt_zero != 0:
    #         nums[:-cnt_zero], nums[-cnt_zero:] = list_non_zero, [0] * cnt_zero

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Runtime:138 ms, faster than 86.81% of Python3 online submissions.
        Memory Usage:17.9 MB, less than 54.89% of Python3 online submissions.

        Follow up: Could you minimize the total number of operations done?
        """

        cur_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_pos] = nums[i]
                cur_pos += 1

        # nums[cur_pos:] = [0] * (len(nums) - cur_pos)
        # OR
        for i in range(cur_pos, len(nums)):
            nums[i] = 0

# leetcode submit region end(Prohibit modification and deletion)
