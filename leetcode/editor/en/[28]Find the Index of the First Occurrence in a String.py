# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
# 
#  Related Topics Two Pointers String String Matching 👍 5603 👎 381


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        return -1


    def strStr(self, haystack: str, needle: str) -> int:
        """
        Runtime:34 ms, faster than 64.25% of Python3 online submissions.
        Memory Usage:16.5 MB, less than 43.05% of Python3 online submissions.
        """
        idx = haystack.find(needle)
        return idx

# leetcode submit region end(Prohibit modification and deletion)
