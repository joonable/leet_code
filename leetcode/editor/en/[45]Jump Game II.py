# You are given a 0-indexed array of integers nums of length n. You are 
# initially positioned at nums[0]. 
# 
#  Each element nums[i] represents the maximum length of a forward jump from 
# index i. In other words, if you are at nums[i], you can jump to any nums[i + j] 
# where: 
# 
#  
#  0 <= j <= nums[i] and 
#  i + j < n 
#  
# 
#  Return the minimum number of jumps to reach nums[n - 1]. The test cases are 
# generated such that you can reach nums[n - 1]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  It's guaranteed that you can reach nums[n - 1]. 
#  
# 
#  Related Topics Array Dynamic Programming Greedy 👍 15443 👎 650


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        n_jump = 0
        jump_pos = 0
        max_jump_pos = 0

        for pos, num in enumerate(nums[:-1]):
            max_jump_pos = max(pos + num, max_jump_pos)
            if jump_pos <= pos:
                n_jump += 1
                jump_pos = max_jump_pos
                if jump_pos >= n - 1:
                    return n_jump
        return n_jump

    def jump_v2(self, nums: List[int]) -> int:
        curr_pos = 0
        n_jump = 0
        next_pos = 0
        for pos, jump in enumerate(nums[:-1]):   # important
            next_pos = max(next_pos, pos + jump)     # important
            if curr_pos == pos: # important
                curr_pos = next_pos
                n_jump += 1
        return n_jump

# leetcode submit region end(Prohibit modification and deletion)
