# Given a string s which represents an expression, evaluate this expression and 
# return its value. 
# 
#  The integer division should truncate toward zero. 
# 
#  You may assume that the given expression is always valid. All intermediate 
# results will be in the range of [-2³¹, 2³¹ - 1]. 
# 
#  Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval(). 
# 
#  
#  Example 1: 
#  Input: s = "3+2*2"
# Output: 7
#  
#  Example 2: 
#  Input: s = " 3/2 "
# Output: 1
#  
#  Example 3: 
#  Input: s = " 3+5 / 2 "
# Output: 5
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s consists of integers and operators ('+', '-', '*', '/') separated by some 
# number of spaces. 
#  s represents a valid expression. 
#  All the integers in the expression are non-negative integers in the range [0,
#  2³¹ - 1]. 
#  The answer is guaranteed to fit in a 32-bit integer. 
#  
# 
#  Related Topics Math String Stack 👍 6375 👎 907


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = '+'

        for ch in s + '+':
            if ch == ' ':
                continue
            elif ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1 * num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch

        return sum(stack)
# leetcode submit region end(Prohibit modification and deletion)
