# Given an integer n, return the least number of perfect square numbers that 
# sum to n. 
# 
#  A perfect square is an integer that is the square of an integer; in other 
# words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 
# are perfect squares while 3 and 11 are not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁴ 
#  
# 
#  Related Topics Math Dynamic Programming Breadth-First Search 👍 11431 👎 480


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
import math
class Solution:
    def numSquares(self, n: int) -> int:
        max_sqrt = int(math.sqrt(n))
        dp = [0] + [math.inf] * n
        for i in range(1, max_sqrt+1):
            sqr = i * i
            for j in range(sqr, n + 1):
                dp[j] = min(dp[j], dp[j - sqr] + 1)

        return dp[n]


        # leetcode submit region end(Prohibit modification and deletion)
