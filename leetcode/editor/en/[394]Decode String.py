# Given an encoded string, return its decoded string. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed to 
# be a positive integer. 
# 
#  You may assume that the input string is always valid; there are no extra 
# white spaces, square brackets are well-formed, etc. Furthermore, you may assume 
# that the original data does not contain any digits and that digits are only for 
# those repeat numbers, k. For example, there will not be input like 3a or 2[4]. 
# 
#  The test cases are generated so that the length of the output will never 
# exceed 10⁵. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 30 
#  s consists of lowercase English letters, digits, and square brackets '[]'. 
#  s is guaranteed to be a valid input. 
#  All the integers in s are in the range [1, 300]. 
#  
# 
#  Related Topics String Stack Recursion 👍 13263 👎 651


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []

        cur_str = ''
        cur_num = ''

        for ch in s:
            if ch.isdigit():
                cur_num += ch
            elif ch == '[':
                str_stack.append(cur_str)
                num_stack.append(int(cur_num))
                cur_str = ''
                cur_num = ''
            elif ch == ']':
                prev_str = str_stack.pop()
                repeat = num_stack.pop()
                cur_str = prev_str + repeat * cur_str
            else:
                cur_str += ch

        return cur_str
        
# leetcode submit region end(Prohibit modification and deletion)
