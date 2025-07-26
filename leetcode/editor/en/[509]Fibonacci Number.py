# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is, 
# 
#  
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#  
# 
#  Given n, calculate F(n). 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 30 
#  
# 
#  Related Topics Math Dynamic Programming Recursion Memoization 👍 8536 👎 380


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib_topdown(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i < 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)

    def fib_bottomup(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# leetcode submit region end(Prohibit modification and deletion)
