# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting 👍 4886 👎 496


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
            Runtime:53 ms, faster than 69.07% of Python3 online submissions.
            Memory Usage:16.7 MB, less than 45.79% of Python3 online submissions.
        """
        magazine_counter = Counter(magazine)
        for ch in ransomNote:
            if magazine_counter[ch] == 0:
                return False
            magazine_counter[ch] -= 1
        return True


    def canConstruct_v2(self, ransomNote: str, magazine: str) -> bool:
        needs = Counter(magazine)
        for ch in ransomNote:
            needs[ch] -= 1
            if needs[ch] < 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
