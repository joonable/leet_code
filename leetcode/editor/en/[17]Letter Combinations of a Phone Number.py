# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digits to letters (just like on the telephone buttons) is given 
# below. Note that 1 does not map to any letters. 
#  
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
# 
#  Related Topics Hash Table String Backtracking 👍 19306 👎 1047


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map_digit_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        return ["".join(l) for l in product(*[map_digit_letter[str(digit)] for digit in digits])]
# leetcode submit region end(Prohibit modification and deletion)
