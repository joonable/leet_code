# There is an integer array nums sorted in ascending order (with distinct 
# values). 
# 
#  Prior to being passed to your function, nums is possibly rotated at an 
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k]
# , nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For 
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0
# ,1,2]. 
# 
#  Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  
#  Example 2: 
#  Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#  
#  Example 3: 
#  Input: nums = [1], target = 0
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -10⁴ <= nums[i] <= 10⁴ 
#  All values of nums are unique. 
#  nums is an ascending array that is possibly rotated. 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search 👍 27725 👎 1685


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        # n = len(nums)
        # if n == 1:
        #     return 0 if nums[0] == target else -1

        # pivot = 0
        # if nums[0] > nums[-1]:  # rotated
        #     left, right = 0, n - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if mid == 0:
        #             left += 1
        #             continue
        #         if nums[mid] < nums[0] and nums[mid - 1] >= nums[0]:
        #             pivot = mid
        #             break
        #         elif nums[mid] < nums[0]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #     nums = nums[pivot:] + nums[:pivot]

        # left, right = 0, n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return (mid + pivot) % n
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return -1
        
# leetcode submit region end(Prohibit modification and deletion)
