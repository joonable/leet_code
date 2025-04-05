# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  Related Topics String Stack 👍 23630 👎 1699

from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    Runtime:33 ms, faster than 73.91% of Python3 online submissions.
    Memory Usage:16.6 MB, less than 74.88% of Python3 online submissions.
    """
    def isValid(self, s: str) -> bool:
        # dq = deque()
        # for ch in s:
        #     if ch in ["(", "[", "{"]:
        #         dq.append(ch)
        #     else:
        #         if not dq:
        #             return False
        #         p = dq.pop()
        #         if ch == ")" and p != "(":
        #             return False
        #         elif ch == "}" and p != "{":
        #             return False
        #         elif ch == "]" and p != "[":
        #             return False
        # return True if not dq else False
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        open_brackets = matching.values()
        for ch in s:
            if ch in open_brackets:  # 여는 괄호
                stack.append(ch)
            else:
                if not stack or stack.pop() != matching[ch]:
                    return False
        return not stack



