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
        if len(s2) < len(s1):
            return False

        needs = Counter(s1)
        window_size = len(s1)
        window = defaultdict(int)
        matched = 0

        left = 0
        for right, right_ch in enumerate(s2):
            if right_ch in needs:
                window[right_ch] += 1
                if window[right_ch] == needs[right_ch]:
                    matched += 1

            if right >= window_size:
                left_ch = s2[left]
                if left_ch in needs:
                    if window[left_ch] == needs[left_ch]:
                        matched -= 1
                    window[left_ch] -= 1
                left += 1

            if matched == len(needs):
                return True

        return False


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        need = Counter(s1)
        window = defaultdict(int)
        window_size = len(s1)

        matched = 0

        for i in range(len(s2)):
            ch = s2[i]
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    matched += 1

            if i - window_size >= 0:
                prev_ch = s2[i - window_size]
                if prev_ch in need:
                    if window[prev_ch] == need[prev_ch]:
                        matched -= 1
                    window[prev_ch] -= 1

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
