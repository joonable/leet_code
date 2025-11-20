# Given a string expression of numbers and operators, return all possible 
# results from computing all the different possible ways to group numbers and operators.
#  You may return the answer in any order. 
# 
#  The test cases are generated such that the output values fit in a 32-bit 
# integer and the number of different results does not exceed 10⁴. 
# 
#  
#  Example 1: 
# 
#  
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
#  
# 
#  Example 2: 
# 
#  
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= expression.length <= 20 
#  expression consists of digits and the operator '+', '-', and '*'. 
#  All the integer values in the input expression are in the range [0, 99]. 
#  The integer values in the input expression do not have a leading '-' or '+' 
# denoting the sign. 
#  
# 
#  Related Topics Math String Dynamic Programming Recursion Memoization 👍 6274 
# 👎 395


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {'+', '-', '*'}
        dict_memories = {}

        def dq(substring: str):
            results = []
            if substring in dict_memories:
                return dict_memories[substring]

            for i, ch in enumerate(substring):
                if ch in operators:
                    left = substring[:i]
                    right = substring[i + 1:]
                    op = substring[i]

                    left_results = dq(left)
                    right_results = dq(right)
                    for l in left_results:
                        for r in right_results:
                            if op == "+":
                                result = l + r
                            elif op == "*":
                                result = l * r
                            else:
                                result = l - r
                            results.append(result)

            if not results:
                results = [int(substring)]

            dict_memories[substring] = results
            return results

        return dq(expression)
        
# leetcode submit region end(Prohibit modification and deletion)
