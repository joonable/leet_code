# Given a string s, find the length of the longest substring without repeating 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 40996 👎 1979


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s < 2:
            return len_s

        max_len = 0
        dict_cnt = {}
        ptr_l, ptr_r = 0, 1
        dict_cnt[s[0]] = 1

        while True:
            if ptr_r == len_s:
                break

            ch_r = s[ptr_r]
            dict_cnt[ch_r] = dict_cnt.get(ch_r, 0) + 1

            if dict_cnt[ch_r] == 2:
                while True:
                    ch_l = s[ptr_l]
                    if ptr_l == ptr_r or ptr_l == len_s:
                        break
                    dict_cnt[ch_l] -= 1
                    if ch_r == ch_l:
                        ptr_l += 1
                        break
                    ptr_l += 1

            max_len = max(max_len, ptr_r - ptr_l + 1)
            ptr_r += 1

        return max_len
