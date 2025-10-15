# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
# 
#  Related Topics Math Dynamic Programming Memoization 👍 22709 👎 913


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


    def climbStairs_dp(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
