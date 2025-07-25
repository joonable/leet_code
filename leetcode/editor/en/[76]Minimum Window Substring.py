# Given two strings s and t of lengths m and n respectively, return the minimum 
# window substring of s such that every character in t (including duplicates) is 
# included in the window. If there is no such substring, return the empty string 
# "". 
# 
#  The testcases will be generated such that the answer is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
# from string t.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == s.length 
#  n == t.length 
#  1 <= m, n <= 10⁵ 
#  s and t consist of uppercase and lowercase English letters. 
#  
# 
#  
#  Follow up: Could you find an algorithm that runs in O(m + n) time? 
# 
#  Related Topics Hash Table String Sliding Window 👍 18731 👎 778


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        matched = 0
        left = 0
        result = ""

        for right, ch in enumerate(s):
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    matched += 1

            while matched == len(need):
                if not result or len(result) > right - left:    # important
                    result = s[left:right + 1]

                left_ch = s[left]
                if left_ch in need:
                    if window[left_ch] == need[left_ch]:
                        matched -= 1
                    window[left_ch] -= 1
                left += 1
        return result

# leetcode submit region end(Prohibit modification and deletion)
