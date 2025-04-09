# Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
# or false otherwise. 
# 
#  In other words, return true if one of s1's permutations is the substring of 
# s2. 
# 
#  
#  Example 1: 
# 
#  
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 and s2 consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table Two Pointers String Sliding Window 👍 12214 👎 476


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = defaultdict(int)
        for ch in s1:
            need[ch] += 1

        window = defaultdict(int)
        matched = 0
        left = 0

        for right in range(len(s2)):
            char = s2[right]
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    matched += 1

            # 윈도우 사이즈 고정: s1과 같은 길이
            if right >= len(s1):
                left_char = s2[left]
                if left_char in need:
                    if window[left_char] == need[left_char]:
                        matched -= 1
                    window[left_char] -= 1
                left += 1

            if matched == len(need):
                return True

        return False
        # len_s1 = len(s1)
        # len_s2 = len(s2)
        # need = Counter(s1)
        # window = Counter(s2[:len_s1])
        #
        # if need == window:
        #     return True
        #
        # for idx in range(len_s1, len_s2):
        #     left = s2[idx - len_s1]
        #     right = s2[idx]
        #     window[left] -= 1
        #     window[right] += 1
        #     if window[left] == 0:
        #         del window[left]
        #
        #     if need == window:
        #         return True
        #
        # return False

# leetcode submit region end(Prohibit modification and deletion)
