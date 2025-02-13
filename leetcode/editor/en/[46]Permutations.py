# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
# 
#  Related Topics Array Backtracking 👍 19645 👎 347


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        len_nums = len(nums)
        def backtrack(path):
            # print(path)
            if len_nums == len(path):
                # print(path)
                result.append(path[:])
            elif len_nums > len(path):
                for i in range(len(nums)):
                    if nums[i] in path:
                        pass
                    else:
                        path.append(nums[i])
                        backtrack(path)
                        path.pop()
        backtrack([])
        return result
# leetcode submit region end(Prohibit modification and deletion)
