# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 10991 👎 344


# leetcode submit region begin(Prohibit modification and deletion)

from collections import Counter

from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        needs = Counter(s)
        counter = defaultdict(int)

        matched = 0
        for ch in t:
            if ch not in needs:
                return False

            counter[ch] += 1
            if counter[ch] == needs[ch]:
                matched += 1
            elif counter[ch] > needs[ch]:
                return False

        return matched == len(needs)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Success:
            Runtime:42 ms, faster than 95.08% of Python3 online submissions.
            Memory Usage:16.7 MB, less than 66.88% of Python3 online submissions.
        """
        if len(s) != len(t):
            return False
        counter_s, counter_t = Counter(s), Counter(t)
        for ch in counter_s.keys():
            if counter_s[ch] != counter_t[ch]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
