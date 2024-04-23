# Given a pattern and a string s, find if s follows the same pattern. 
# 
#  Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length <= 300 
#  pattern contains only lower-case English letters. 
#  1 <= s.length <= 3000 
#  s contains only lowercase English letters and spaces ' '. 
#  s does not contain any leading or trailing spaces. 
#  All the words in s are separated by a single space. 
#  
# 
#  Related Topics Hash Table String 👍 7156 👎 983


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Runtime:32 ms, faster than 74.63% of Python3 online submissions.
        Memory Usage:16.7 MB, less than 14.41% of Python3 online submissions.
        """
        if len(list(pattern)) != len(s.split()):
            return False

        dict_ptrn_word = {}
        dict_word_ptrn = {}

        for ptrn, word in zip(list(pattern), s.split()):
            saved_word = dict_ptrn_word.get(ptrn, None)
            saved_ptrn = dict_word_ptrn.get(word, None)

            if not saved_word:
                dict_ptrn_word[ptrn] = word
            else:
                if saved_word != word:
                    return False

            if not saved_ptrn:
                dict_word_ptrn[word] = ptrn
            else:
                if saved_ptrn != ptrn:
                    return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
