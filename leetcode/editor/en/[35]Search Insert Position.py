# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be if it were 
# inserted in order. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums contains distinct values sorted in ascending order. 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search 👍 10893 👎 515


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]: return 0
        if nums[-1] < target: return len(nums)

        def binary_search(left, right):
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                if nums[pivot - 1] < target < nums[pivot]:
                    return pivot
                else:
                    return binary_search(left, pivot)
            elif target > nums[pivot]:
                if nums[pivot] < target < nums[pivot + 1]:
                    return pivot + 1
                else:
                    return binary_search(pivot, right)

        return binary_search(0, len(nums) + 1)
