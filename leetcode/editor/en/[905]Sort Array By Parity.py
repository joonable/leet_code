# Given an integer array nums, move all the even integers at the beginning of 
# the array followed by all the odd integers. 
# 
#  Return any array that satisfies this condition. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be 
# accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  0 <= nums[i] <= 5000 
#  
# 
#  Related Topics Array Two Pointers Sorting 👍 5600 👎 156


# leetcode submit region begin(Prohibit modification and deletion)
# from collections import deque
class Solution:
    #     def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #         dq = deque([])
    #         for num in nums:
    #             if num % 2 == 0:
    #                 dq.appendleft(num)
    #             else:
    #                 dq.append(num)
    #         return list(dq)

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Sorts array so that all even numbers appear before odd numbers.
        Uses two-pointer technique to swap elements in-place.

        Args:
            nums: List of integers to be sorted by parity

        Returns:
            The modified array with even numbers first, then odd numbers
        """
        # Initialize two pointers: left starts at beginning, right at end
        left = 0
        right = len(nums) - 1

        # Continue until pointers meet
        while left < right:
            # If left element is even, it's in correct position, move left pointer forward
            if nums[left] % 2 == 0:
                left += 1
            # If right element is odd, it's in correct position, move right pointer backward
            elif nums[right] % 2 == 1:
                right -= 1
            # If left is odd and right is even, swap them and move both pointers
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
# leetcode submit region end(Prohibit modification and deletion)
