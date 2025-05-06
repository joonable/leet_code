# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums is a non-decreasing array. 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics Array Binary Search 👍 21665 👎 570


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_left: bool) -> int:   # important
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if is_left:
                        if mid == 0 or nums[mid - 1] < target:
                            return mid
                        right = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] > target:  # important
                            return mid
                        left = mid + 1
            return -1

        left_index = find_bound(True)
        if left_index == -1:
            return [-1, -1]
        right_index = find_bound(False)
        return [left_index, right_index]
# leetcode submit region end(Prohibit modification and deletion)
