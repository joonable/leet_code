# You are given an integer array nums consisting of n elements, and an integer 
# k. 
# 
#  Find a contiguous subarray whose length is equal to k that has the maximum 
# average value and return this value. Any answer with a calculation error less 
# than 10⁻⁵ will be accepted. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5], k = 1
# Output: 5.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= k <= n <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Sliding Window 👍 3307 👎 287


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Runtime:860 ms, faster than 93.77% of Python3 online submissions.
        Memory Usage:28.3 MB, less than 91.02% of Python3 online submissions.
        """
        length = len(nums)
        max_sum = sum(nums[0:k])
        sub_sum = sum(nums[0:k])

        for i in range(1, length-k+1):
            sub_sum = sub_sum - nums[i-1] + nums[i+k-1]
            if sub_sum > max_sum:
                max_sum = sub_sum
        return max_sum/k


# leetcode submit region end(Prohibit modification and deletion)
