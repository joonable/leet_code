# For two strings s and t, we say "t divides s" if and only if s = t + t + t + .
# .. + t + t (i.e., t is concatenated with itself one or more times). 
# 
#  Given two strings str1 and str2, return the largest string x such that x 
# divides both str1 and str2. 
# 
#  
#  Example 1: 
# 
#  
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#  
# 
#  Example 2: 
# 
#  
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#  
# 
#  Example 3: 
# 
#  
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= str1.length, str2.length <= 1000 
#  str1 and str2 consist of English uppercase letters. 
#  
# 
#  Related Topics Math String 👍 4814 👎 1178


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Runtime:31 ms, faster than 88.96% of Python3 online submissions.
        Memory Usage:16.6 MB, less than 64.49% of Python3 online submissions.
        """
        len1 = len(str1)
        len2 = len(str2)
        length = min(len1, len2)
        gcd = 0
        for i in range(length, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                gcd = i
                break

        if not gcd:
            return ""

        str_gcd = str1[:gcd]
        for i in range(0, len1, gcd):
            if str_gcd != str1[i:i+gcd]:
                return ""
        for j in range(0, len2, gcd):
            if str_gcd != str2[j:j+gcd]:
                return ""

        return str_gcd
# leetcode submit region end(Prohibit modification and deletion)
