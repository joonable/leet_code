# You are given an array of strings tokens that represents an arithmetic 
# expression in a Reverse Polish Notation. 
# 
#  Evaluate the expression. Return an integer that represents the value of the 
# expression. 
# 
#  Note that: 
# 
#  
#  The valid operators are '+', '-', '*', and '/'. 
#  Each operand may be an integer or another expression. 
#  The division between two integers always truncates toward zero. 
#  There will not be any division by zero. 
#  The input represents a valid arithmetic expression in a reverse polish 
# notation. 
#  The answer and all the intermediate calculations can be represented in a 32-
# bit integer. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#  
# 
#  Example 2: 
# 
#  
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#  
# 
#  Example 3: 
# 
#  
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tokens.length <= 10⁴ 
#  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
# range [-200, 200]. 
#  
# 
#  Related Topics Array Math Stack 👍 8053 👎 1133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        digit_stack = []
        operators = {"-", "+", "/", "*"}

        for t in tokens:
            if t in operators:
                y = digit_stack.pop()
                x = digit_stack.pop()
                if t == "-":
                    val = x - y
                elif t == '+':
                    val = x + y
                elif t == '*':
                    val = x * y
                else:
                    val = int(x / y)
                digit_stack.append(val)
            else:
                digit_stack.append(int(t))
        return digit_stack[0]
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     for token in tokens:
    #         if token.lstrip('-').isdigit():   # important
    #             stack.append(int(token))
    #         else:
    #             num2 = stack.pop()
    #             num1 = stack.pop()
    #             if token == "*":
    #                 x = num1 * num2
    #             elif token == "-":
    #                 x = num1 - num2
    #             elif token == "/":
    #                 x = int(num1 / num2)
    #             elif token == "+":
    #                 x = num1 + num2
    #             stack.append(x)
    #     return stack[-1]
        
# leetcode submit region end(Prohibit modification and deletion)
