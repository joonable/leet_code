# Given an integer array nums, return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i]. 
# 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
# 
#  You must write an algorithm that runs in O(n) time and without using the 
# division operation. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#  
#  Example 2: 
#  Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#  
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  The input is generated such that answer[i] is guaranteed to fit in a 32-bit 
# integer. 
#  
# 
#  
#  Follow up: Can you solve the problem in O(1) extra space complexity? (The 
# output array does not count as extra space for space complexity analysis.) 
# 
#  Related Topics Array Prefix Sum 👍 24085 👎 1550


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left_mul = 1    # important
        right_mul = 1
        for left in range(n):
            right = n - left - 1
            answer[left] *= left_mul    # important
            answer[right] *= right_mul
            left_mul *= nums[left]  # important
            right_mul *= nums[right]
        return answer
# leetcode submit region end(Prohibit modification and deletion)
