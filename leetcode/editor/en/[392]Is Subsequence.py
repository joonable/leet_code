# Given two strings s and t, return true if s is a subsequence of t, or false 
# otherwise. 
# 
#  A subsequence of a string is a new string that is formed from the original 
# string by deleting some (can be none) of the characters without disturbing the 
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
# "abcde" while "aec" is not). 
# 
#  
#  Example 1: 
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#  
#  Example 2: 
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10⁴ 
#  s and t consist only of lowercase English letters. 
#  
# 
#  
# Follow up: Suppose there are lots of incoming 
# s, say 
# s1, s2, ..., sk where 
# k >= 10⁹, and you want to check one by one to see if 
# t has its subsequence. In this scenario, how would you change your code?
# 
#  Related Topics Two Pointers String Dynamic Programming 👍 6442 👎 362


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        slice_idx = 0
        for s_idx, _s in enumerate(list_s):
            if _s in list_t[slice_idx:]:
                t_idx = list_t[slice_idx:].index(_s) + slice_idx
                if t_idx < slice_idx:
                    return False
                else:
                    slice_idx = t_idx
                slice_idx += 1
            else:
                return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
