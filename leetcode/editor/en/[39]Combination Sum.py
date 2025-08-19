# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order. 
# 
#  The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen 
# numbers is different. 
# 
#  The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple 
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#  
# 
#  Example 3: 
# 
#  
# Input: candidates = [2], target = 1
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 30 
#  2 <= candidates[i] <= 40 
#  All elements of candidates are distinct. 
#  1 <= target <= 40 
#  
# 
#  Related Topics Array Backtracking 👍 19510 👎 454


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []
        combination = []
        sum_combination = 0

        def backtracking(idx):
            nonlocal sum_combination
            if sum_combination == target:
                result.append(combination[:])

            for i in range(idx, n):
                candidate = candidates[i]
                if candidate + sum_combination > target:
                    break

                combination.append(candidate)
                sum_combination += candidate
                backtracking(i)
                combination.pop()
                sum_combination -= candidate

        backtracking(0)
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(idx, path):
            current_sum = sum(path)
            if current_sum == target:
                result.append(path[:])
            elif current_sum < target:
                for i in range(idx, len(candidates)):
                    path.append(candidates[i])
                    backtrack(i, path)
                    path.pop()
        backtrack(0, [])
        return result


# leetcode submit region end(Prohibit modification and deletion)
