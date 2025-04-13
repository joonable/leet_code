# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,0,1,2]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Hash Table Union Find 👍 21209 👎 1133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        set_nums = set(nums) # important
        for num in set_nums: # important
            if not num - 1 in set_nums: # important
                length = 1
                while num + length in set_nums:
                    length += 1
                max_len = max(max_len, length)
        return max_len
        
# leetcode submit region end(Prohibit modification and deletion)
