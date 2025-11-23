# Given an integer array nums, find a subarray that has the largest product, 
# and return the product. 
# 
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# 
#  Note that the product of an array with a single element is the value of that 
# element. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
#  
#  
# 
#  Related Topics Array Dynamic Programming 👍 19996 👎 809


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max_prod = min_prod = nums[0]
        for num in nums[1:]:
            new_min_prod = min(num, min_prod * num, max_prod * num)
            new_max_prod = max(num, min_prod * num, max_prod * num)
            max_prod = new_max_prod
            min_prod = new_min_prod
            result = max(new_max_prod, result)
        return result
# leetcode submit region end(Prohibit modification and deletion)
