# Given an integer n, return true if it is a power of two. Otherwise, return 
# false. 
# 
#  An integer n is a power of two, if there exists an integer x such that n == 2
# ˣ. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: true
# Explanation: 2⁰ = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 16
# Output: true
# Explanation: 2⁴ = 16
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= n <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without loops/recursion?
# 
#  Related Topics Math Bit Manipulation Recursion 👍 7976 👎 502


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and n & (n - 1) == 0
        
# leetcode submit region end(Prohibit modification and deletion)
