# Write a function that reverses a string. The input string is given as an 
# array of characters s. 
# 
#  You must do this by modifying the input array in-place with O(1) extra 
# memory. 
# 
#  
#  Example 1: 
#  Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  
#  Example 2: 
#  Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is a printable ascii character. 
#  
# 
#  Related Topics Two Pointers String 👍 8044 👎 1137


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Success:
            Runtime:179 ms, faster than 97.62% of Python3 online submissions.
            Memory Usage:20.8 MB, less than 29.47% of Python3 online submissions.
        """
        s.reverse()
        # s[:] = s[::-1]


# leetcode submit region end(Prohibit modification and deletion)
