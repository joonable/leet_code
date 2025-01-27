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
# TODO
class Solution:
    def climbStairs(self, n: int) -> int:
        prev_1, prev_2 = 1, 1
        for _ in range(2, n+1):
            dp = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = dp
        return prev_1
# leetcode submit region end(Prohibit modification and deletion)
