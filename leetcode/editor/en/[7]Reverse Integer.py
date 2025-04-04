# Given a signed 32-bit integer x, return x with its digits reversed. If 
# reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed 
# or unsigned). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: x = -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: x = 120
# Output: 21
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  Related Topics Math 👍 12128 👎 13134


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x < -2**31 or x > 2**31 - 1:
            return 0
        elif x > 0:
            s = str(x)[::-1]
            result = int(s)
        else:
            s = str(x)[1:][::-1]
            result = int(s) * -1

        return 0 if int.bit_length(result) >= 32 else result


    # def reverse(self, x: int) -> int:
    #     """
    #     Success:
    #         Runtime:31 ms, faster than 95.35% of Python3 online submissions.
    #         Memory Usage:16.2 MB, less than 70.90% of Python3 online submissions.
    #     """
    #     # if x <= -2 ** 31 or x >= 2 ** 31 - 1:
    #     #     return 0
    #     if x >= 0:
    #         result = str(x)[::-1]
    #     else:
    #         x *= -1
    #         result = "-" + str(x)[::-1]
    #
    #     result = int(result)
    #
    #     return 0 if int.bit_length(result) >= 32 else result
# leetcode submit region end(Prohibit modification and deletion)
