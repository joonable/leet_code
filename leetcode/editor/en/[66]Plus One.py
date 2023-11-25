# You are given a large integer represented as an integer array digits, where 
# each digits[i] is the iᵗʰ digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. The large integer does 
# not contain any leading 0's. 
# 
#  Increment the large integer by one and return the resulting array of digits. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  digits does not contain any leading 0's. 
#  
# 
#  Related Topics Array Math 👍 8583 👎 5251


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Success:
            Runtime:38 ms, faster than 72.72% of Python3 online submissions.
            Memory Usage:16.2 MB, less than 35.64% of Python3 online submissions.
        """
        result = "".join([str(x) for x in digits])
        result = [int(x) for x in str(int(result) + 1)]
        return result
        # return [int(x) for x in str(int("".join([str(x) for x in digits])) + 1)]


    # def plusOne(self, digits: list[int]) -> list[int]:
    #     """
    #     Runtime:44 ms, faster than 25.77% of Python3 online submissions.
    #     Memory Usage:16.3 MB, less than 6.21% of Python3 online submissions.
    #     """
    #     num = 0
    #     for i in reversed(range(len(digits))):
    #         num += digits[i] * 10 ** (len(digits) - i - 1)
    #     list_num = [int(x) for x in str(num+1)]
    #     return list_num


    # def plusOne(self, digits: list[int]) -> list[int]:
    #     """
    #     Success:
    #     Runtime:40 ms, faster than 54.63% of Python3 online submissions.
    #     Memory Usage:16.5 MB, less than 6.21% of Python3 online submissions.
    #     """
    #     carry = 1
    #     for i in reversed(range(len(digits))):
    #         digits[i] += carry
    #         carry = digits[i] // 10
    #         digits[i] %= 10
    #
    #     if carry:
    #         digits = [1] + digits
    #
    #     return digits
