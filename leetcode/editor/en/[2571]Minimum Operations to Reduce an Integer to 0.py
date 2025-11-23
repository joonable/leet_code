# You are given a positive integer n, you can do the following operation any 
# number of times: 
# 
#  
#  Add or subtract a power of 2 from n. 
#  
# 
#  Return the minimum number of operations to make n equal to 0. 
# 
#  A number x is power of 2 if x == 2ⁱ where i >= 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 39
# Output: 3
# Explanation: We can do the following operations:
# - Add 2⁰ = 1 to n, so now n = 40.
# - Subtract 2³ = 8 from n, so now n = 32.
# - Subtract 2⁵ = 32 from n, so now n = 0.
# It can be shown that 3 is the minimum number of operations we need to make n 
# equal to 0.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 54
# Output: 3
# Explanation: We can do the following operations:
# - Add 2¹ = 2 to n, so now n = 56.
# - Add 2³ = 8 to n, so now n = 64.
# - Subtract 2⁶ = 64 from n, so now n = 0.
# So the minimum number of operations is 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁵ 
#  
# 
#  Related Topics Dynamic Programming Greedy Bit Manipulation 👍 596 👎 196


# leetcode submit region begin(Prohibit modification and deletion)
from math import log2
class Solution:
    def minOperations(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            i = int(log2(n))
            n = min(n - 2 ** i, 2 ** (i + 1) - n)
            if n == 0:
                return cnt
        return -1
# leetcode submit region end(Prohibit modification and deletion)
