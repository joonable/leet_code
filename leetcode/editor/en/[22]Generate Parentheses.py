# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics String Dynamic Programming Backtracking 👍 21786 👎 1008


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtracking(n_open, n_close, s):
            if len(s) == 2 * n:
                result.append(s)
            if n_open < n:
                backtracking(n_open + 1, n_close, s + "(")
            if n_close < n_open:
                backtracking(n_open, n_close + 1, s + ")")
        backtracking(0, 0, "")
        return result

# leetcode submit region end(Prohibit modification and deletion)
