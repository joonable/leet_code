# You are given two strings word1 and word2. Merge the strings by adding 
# letters in alternating order, starting with word1. If a string is longer than the 
# other, append the additional letters onto the end of the merged string. 
# 
#  Return the merged string. 
# 
#  
#  Example 1: 
# 
#  
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
#  
# 
#  Example 3: 
# 
#  
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word1.length, word2.length <= 100 
#  word1 and word2 consist of lowercase English letters. 
#  
# 
#  Related Topics Two Pointers String 👍 3533 👎 76


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Runtime:35 ms, faster than 64.05% of Python3 online submissions.
        Memory Usage:16.4 MB, less than 95.76% of Python3 online submissions.
        """
        len1 = len(word1)
        len2 = len(word2)
        length = len1 + len2
        result = ["" for _ in range(length)]
        pos1 = 0
        pos2 = 0
        pos = 0

        while pos1 < len1 or pos2 < len2:
            if pos1 < len1:
                result[pos] = word1[pos1]
                pos1 += 1
                pos += 1

            if pos2 < len2:
                result[pos] = word2[pos2]
                pos2 += 1
                pos += 1

        return "".join(result)
# leetcode submit region end(Prohibit modification and deletion)
