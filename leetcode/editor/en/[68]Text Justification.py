# Given an array of strings words and a width maxWidth, format the text such 
# that each line has exactly maxWidth characters and is fully (left and right) 
# justified. 
# 
#  You should pack your words in a greedy approach; that is, pack as many words 
# as you can in each line. Pad extra spaces ' ' when necessary so that each line 
# has exactly maxWidth characters. 
# 
#  Extra spaces between words should be distributed as evenly as possible. If 
# the number of spaces on a line does not divide evenly between words, the empty 
# slots on the left will be assigned more spaces than the slots on the right. 
# 
#  For the last line of text, it should be left-justified, and no extra space 
# is inserted between words. 
# 
#  Note: 
# 
#  
#  A word is defined as a character sequence consisting of non-space characters 
# only. 
#  Each word's length is guaranteed to be greater than 0 and not exceed 
# maxWidth. 
#  The input array words contains at least one word. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."]
# , maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ] 
# 
#  Example 2: 
# 
#  
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 
# 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one 
# word. 
# 
#  Example 3: 
# 
#  
# Input: words = ["Science","is","what","we","understand","well","enough","to",
# "explain","to","a","computer.","Art","is","everything","else","we","do"], 
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ] 
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 300 
#  1 <= words[i].length <= 20 
#  words[i] consists of only English letters and symbols. 
#  1 <= maxWidth <= 100 
#  words[i].length <= maxWidth 
#  
# 
#  Related Topics Array String Simulation 👍 4124 👎 5076


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_words = []
        curr_width = 0
        result = []

        def justify(words, width, is_last):
            n_words = len(words)
            left_width = maxWidth - width
            if n_words == 1 or is_last:
                return " ".join(words) + " " * (left_width - n_words + 1)
            else:
                n_space, mod = divmod(left_width, n_words - 1)
                line = ""
                for i, word in enumerate(words[:-1]):
                    line += word + " " * (n_space + (1 if i < mod else 0))
                return line + words[-1]

        for i, word in enumerate(words):
            if len(word) + len(curr_words) + curr_width > maxWidth:
                result.append(justify(curr_words, curr_width, False))
                curr_words = []
                curr_width = 0
            curr_words.append(word)
            curr_width += len(word)
        result.append(justify(curr_words, curr_width, True))
        return result

# leetcode submit region end(Prohibit modification and deletion)
