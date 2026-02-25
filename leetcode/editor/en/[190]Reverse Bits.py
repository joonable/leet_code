# Reverse bits of a given 32 bits signed integer. 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 43261596 
#  
# 
#  Output: 964176192 
# 
#  Explanation: 
# 
#  
#  
#  
#  Integer 
#  Binary 
#  
#  
#  43261596 
#  00000010100101000001111010011100 
#  
#  
#  964176192 
#  00111001011110000010100101000000 
#  
#  
#  
# 
#  Example 2: 
# 
#  
#  Input: n = 2147483644 
#  
# 
#  Output: 1073741822 
# 
#  Explanation: 
# 
#  
#  
#  
#  Integer 
#  Binary 
#  
#  
#  2147483644 
#  01111111111111111111111111111100 
#  
#  
#  1073741822 
#  00111111111111111111111111111110 
#  
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 2³¹ - 2 
#  n is even. 
#  
# 
#  
#  Follow up: If this function is called many times, how would you optimize it? 
# 
# 
#  Related Topics Divide and Conquer Bit Manipulation 👍 5865 👎 1675


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            if bit:
                result |= (bit << (31 - i))
        return result
# leetcode submit region end(Prohibit modification and deletion)
