# Given a string s and an array of strings words, return the number of words[i] 
# that is a subsequence of s. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order 
# of the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: 
# "a", "acd", "ace".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 50 
#  s and words[i] consist of only lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Binary Search Dynamic Programming 
# Trie Sorting 👍 5743 👎 244


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict_waiting = defaultdict(deque)
        for word in words:
            dict_waiting[word[0]].append(word)

        cnt = 0
        for ch in s:
            for _ in range(len(dict_waiting[ch])):
                word = dict_waiting[ch].popleft()
                if len(word) == 1:
                    cnt += 1
                else:
                    dict_waiting[word[1]].append(word[1:])
        return cnt
        
# leetcode submit region end(Prohibit modification and deletion)
