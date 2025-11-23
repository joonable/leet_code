# You are given an integer array nums. The absolute sum of a subarray [numsl, 
# numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr). 
# 
#  Return the maximum absolute sum of any (possibly empty) subarray of nums. 
# 
#  Note that abs(x) is defined as follows: 
# 
#  
#  If x is a negative integer, then abs(x) = -x. 
#  If x is a non-negative integer, then abs(x) = x. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) =
#  8.
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
#  Related Topics Array Dynamic Programming 👍 1947 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_abs_sum = cur_max_sum = cur_min_sum = nums[0]
        max_abs_sum = abs(max_abs_sum)
        for num in nums[1:]:
            cur_min_sum = min(num, cur_min_sum + num)
            cur_max_sum = max(num, cur_max_sum + num)
            max_abs_sum = max(max_abs_sum, abs(cur_min_sum), abs(cur_max_sum))
        return max_abs_sum
        
# leetcode submit region end(Prohibit modification and deletion)
