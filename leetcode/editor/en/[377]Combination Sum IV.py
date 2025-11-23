# Given an array of distinct integers nums and a target integer target, return 
# the number of possible combinations that add up to target. 
# 
#  The test cases are generated so that the answer can fit in a 32-bit integer. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [9], target = 3
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 1000 
#  All the elements of nums are unique. 
#  1 <= target <= 1000 
#  
# 
#  
#  Follow up: What if negative numbers are allowed in the given array? How does 
# it change the problem? What limitation we need to add to the question to allow 
# negative numbers? 
# 
#  Related Topics Array Dynamic Programming 👍 7698 👎 698


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = [num for num in nums if num <= target]
        if not nums:
            return 0
        dp = [1] + [0] * target

        result = 0
        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]
        return dp[target]
# leetcode submit region end(Prohibit modification and deletion)
