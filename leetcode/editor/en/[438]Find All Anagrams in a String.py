# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s and p consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 12679 👎 351


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)
        necessary = Counter(p)
        windows = defaultdict(int)
        matched = 0

        result = []
        for right, right_ch in enumerate(s):
            # 추가
            if right_ch in necessary:  # important
                windows[right_ch] += 1
                if windows[right_ch] == necessary[right_ch]:
                    matched += 1

            if right >= window_size - 1:  # important
                # 검증
                left = right - window_size + 1
                if matched == len(necessary):
                    result.append(left)

                # 삭제
                left_ch = s[left]
                if left_ch in necessary:
                    if windows[left_ch] == necessary[left_ch]:
                        matched -= 1
                    windows[left_ch] -= 1

        return result

    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     if len(s) < len(p):
    #         return []
    #
    #     need = Counter(p)
    #     window = defaultdict(int)
    #     valid = 0
    #     result = []
    #     window_size = len(p)
    #
    #     for i in range(window_size):
    #         ch = s[i]
    #         if ch in need:
    #             window[ch] += 1
    #             if window[ch] == need[ch]:
    #                 valid += 1
    #
    #     if valid == len(need):
    #         result.append(i - window_size + 1)
    #
    #     for i in range(window_size, len(s)):
    #         ch = s[i]
    #         if ch in need:
    #             window[ch] += 1
    #             if window[ch] == need[ch]:
    #                 valid += 1
    #
    #         prev_ch = s[i - window_size]
    #         if prev_ch in need:
    #             if window[prev_ch] == need[prev_ch]:
    #                 valid -= 1
    #             window[prev_ch] -= 1
    #
    #         if valid == len(need):
    #             result.append(i - window_size + 1)
    #
    #     return result

    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     if len(p) > len(s):
    #         return []
    #
    #     need = Counter(p)
    #     window = defaultdict(int)
    #     valid = 0
    #     result = []
    #
    #     for right in range(len(s)):
    #         ch = s[right]
    #         if ch in need:
    #             window[ch] += 1
    #             if window[ch] == need[ch]:
    #                 valid += 1
    #
    #         # 윈도우 크기가 len(p) 이상이 되면 수축
    #         if right >= len(p):
    #             left = right - len(p)
    #             d = s[left]
    #             if d in need:
    #                 if window[d] == need[d]:
    #                     valid -= 1
    #                 window[d] -= 1
    #
    #         if right >= len(p) - 1 and valid == len(need):
    #             result.append(right - len(p) + 1)
    #
    #     return result
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     result = []
    #     if len(p) > len(s):
    #         return result

    #     need = Counter(p)
    #     window = defaultdict(int)
    #     valid = set()

    #     for i in range(len(p)):
    #         ch = s[i]
    #         if ch in need:
    #             window[ch] += 1
    #             if need[ch] == window[ch]:
    #                 valid.add(ch)
    #             else:
    #                 valid.discard(ch)

    #     for r in range(len(p), len(s)):   # TODO len(s) - len(p) + 1
    #         if len(valid) == len(need):
    #             result.append(r - len(p))

    #         ch_r = s[r]
    #         if ch_r in need:
    #             window[ch_r] += 1
    #             if need[ch_r] == window[ch_r]:
    #                 valid.add(ch_r)
    #             else:
    #                 valid.discard(ch_r)

    #         l = r - len(p)
    #         ch_l = s[l]
    #         if ch_l in need:
    #             window[ch_l] -= 1
    #             if need[ch_l] == window[ch_l]:
    #                 valid.add(ch_l)
    #             else:
    #                 valid.discard(ch_l)

    #     if len(valid) == len(need):
    #         result.append(len(s) - len(p))

    #     return result

    # for l in range(len(s)):   # TODO len(s) - len(p) + 1
    #     ch_r = s[r]
    #     if ch_r in need:
    #         window[ch_r] += 1
    #         if need[ch_r] == window[ch_r]:
    #             valid += 1

    #     if valid == len(need):
    #         result.append(l)

    #     if r > len(p):
    #         ch_l = s[l]
    #         if ch_l in need:
    #             if need[ch_l] == window[ch_l]:
    #                 valid -= 1
    #             window[ch_l] -= 1
    #         l += 1

    # return result

    # while l < len(s) - len(p) + 1:
    #     ch = s[l]
    #     if ch in need:
    #         window[ch] += 1
    #         if need[ch] == window[ch]:
    #             valid += 1

    #         if s[l] in need:
    #             if need[s[l]] == window[s[l]]:
    #                 valid += 1
    #             window[s[l]] -= 1

    #         l += 1
    #     else:
    #         window = defaultdict(int)
    #         valid = 0
    #         l += k

# leetcode submit region end(Prohibit modification and deletion)
