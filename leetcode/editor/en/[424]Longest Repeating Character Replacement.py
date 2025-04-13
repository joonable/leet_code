# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. You can perform 
# this operation at most k times. 
# 
#  Return the length of the longest substring containing the same letter you 
# can get after performing the above operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of only uppercase English letters. 
#  0 <= k <= s.length 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 11559 👎 635


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = Counter()
        max_len = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_count = max(counter.values())

            # window 크기 - 가장 많은 문자 수 > k 라면 왼쪽 이동
            # max_len 구해야 하기 떄문에 window size를 굳이 다시 줄일 필요는 없음
            if (right - left + 1) - max_count > k:
                counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
# leetcode submit region end(Prohibit modification and deletion)
