# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric 
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s consists only of printable ASCII characters. 
#  
# 
#  Related Topics Two Pointers String 👍 8522 👎 8039


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Success:
            Runtime:38 ms, faster than 96.80% of Python3 online submissions.
            Memory Usage:17.9 MB, less than 21.41% of Python3 online submissions.
        """
        s = "".join([ch for ch in s if ch.isalnum()]).lower()
        return s[:] == s[::-1]
# leetcode submit region end(Prohibit modification and deletion)
