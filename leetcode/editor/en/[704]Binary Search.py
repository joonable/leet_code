# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, then 
# return its index. Otherwise, return -1. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ < nums[i], target < 10⁴ 
#  All the integers in nums are unique. 
#  nums is sorted in ascending order. 
#  
# 
#  Related Topics Array Binary Search 👍 7507 👎 162


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            def binary_search(l_pos, r_pos):
                pivot_idx = (l_pos + r_pos) // 2
                # print(l_pos, r_pos, pivot_idx, target, nums[pivot_idx])
                if target < nums[pivot_idx]:
                    return binary_search(l_pos, pivot_idx)
                elif nums[pivot_idx] < target:
                    return binary_search(pivot_idx, r_pos)
                else:
                    return pivot_idx
            return binary_search(0, len(nums))
        else:
            return -1
