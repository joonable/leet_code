# Given a string s consisting of words and spaces, return the length of the 
# last word in the string. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only English letters and spaces ' '. 
#  There will be at least one word in s. 
#  
# 
#  Related Topics String 👍 5067 👎 275


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Runtime:29 ms, faster than 88.56% of Python3 online submissions.
        Memory Usage:16.8 MB, less than 6.15% of Python3 online submissions.
        """
        is_counting = False
        idx = len(s) - 1
        n_char = 0
        while True:
            if idx == -1:
                break

            if not is_counting:
                if s[idx] != " ":
                    is_counting = True
                    n_char += 1
            else:
                if s[idx] == " ":
                    break
                else:
                    n_char += 1

            idx -= 1
        return n_char
# leetcode submit region end(Prohibit modification and deletion)
