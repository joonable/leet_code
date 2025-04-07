# Given a string s of '(' , ')' and lowercase English characters. 
# 
#  Your task is to remove the minimum number of parentheses ( '(' or ')', in 
# any positions ) so that the resulting parentheses string is valid and return any 
# valid string. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, contains only lowercase characters, or 
#  It can be written as AB (A concatenated with B), where A and B are valid 
# strings, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either '(' , ')', or lowercase English letter. 
#  
# 
#  Related Topics String Stack 👍 7135 👎 157


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s

        stack = []
        n_open_bracket = 0

        for ch in s:
            if ch == '(':
                stack.append(ch)
                n_open_bracket += 1
            elif ch == ')':
                if n_open_bracket > 0:
                    stack.append(ch)
                    n_open_bracket -= 1
            else:
                stack.append(ch)

        result = []
        for ch in reversed(stack):
            # for ch in stack:
            # ch = stack.pop()
            if ch == '(' and n_open_bracket > 0:
                n_open_bracket -= 1
                continue
            else:
                result.append(ch)

        return ''.join(result[::-1])

        # stack = []
        # remove_idx = set()

        # for i, ch in enumerate(s):
        #     if ch == '(':
        #         stack.append(i)
        #     elif ch == ')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             remove_idx.add(i)

        # remove_idx.update(stack)

        # result = [ch for i, ch in enumerate(s) if i not in remove_idx]
        # return ''.join(result)

# leetcode submit region end(Prohibit modification and deletion)
