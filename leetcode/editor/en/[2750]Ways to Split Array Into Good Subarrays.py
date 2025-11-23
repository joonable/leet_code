# You are given a binary array nums. 
# 
#  A subarray of an array is good if it contains exactly one element with the 
# value 1. 
# 
#  Return an integer denoting the number of ways to split the array nums into 
# good subarrays. As the number may be too large, return it modulo 10⁹ + 7. 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,0,0,1]
# Output: 3
# Explanation: There are 3 ways to split nums into good subarrays:
# - [0,1] [0,0,1]
# - [0,1,0] [0,1]
# - [0,1,0,0] [1]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0]
# Output: 1
# Explanation: There is 1 way to split nums into good subarrays:
# - [0,1,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 1 
#  
# 
#  Related Topics Array Math Dynamic Programming 👍 465 👎 14


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        start = None
        for i in range(n):
            if nums[i]:
                start = i
                break

        if start is None:
            return 0

        result = 1
        for i in range(start + 1, n):
            if nums[i]:
                result *= i - start
                result %= MOD
                start = i
        return result

    def numberOfGoodSubarraySplits_v2(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        one_idx = [i for i, num in enumerate(nums) if num]
        n = len(one_idx)
        if n <= 1:
            return n

        result = 1
        for i in range(n - 1):
            result = result * (one_idx[i + 1] - one_idx[i]) % MOD
        return result
# leetcode submit region end(Prohibit modification and deletion)
