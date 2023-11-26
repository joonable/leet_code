# Given a string s, find the first non-repeating character in it and return its 
# index. If it does not exist, return -1. 
# 
#  
#  Example 1: 
#  Input: s = "leetcode"
# Output: 0
#  
#  Example 2: 
#  Input: s = "loveleetcode"
# Output: 2
#  
#  Example 3: 
#  Input: s = "aabb"
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Queue Counting 👍 8324 👎 268


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from string import ascii_lowercase
class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     len_s = len(s)
    #     dict_idx = {ch: len_s for ch in ascii_lowercase}
    #     dict_occur = {ch: 0 for ch in ascii_lowercase}
    #
    #     for idx, ch in enumerate(s):
    #         dict_occur[ch] += 1
    #         dict_idx[ch] = idx
    #
    #     list_one = [ch for ch, v in dict_occur.items() if v == 1]
    #     if not list_one:
    #         return -1
    #     dict_idx = {ch: dict_idx[ch] for ch in list_one}
    #     return min(dict_idx.values())

    def firstUniqChar(self, s: str) -> int:
        """
        Success:
            Runtime:83 ms, faster than 86.28% of Python3 online submissions.
            Memory Usage:16.5 MB, less than 58.20% of Python3 online submissions.
        """
        counter = Counter(s)
        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1





    # leetcode submit region end(Prohibit modification and deletion)
