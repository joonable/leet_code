# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
# 
#  Related Topics Array Binary Search Dynamic Programming 👍 21514 👎 471


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     sorted_num_set = sorted(list(set(nums)))
    #     dict_cnt = {}
    #     for n in nums:
    #         max_cnt = 0
    #         for m in sorted_num_set:
    #             if n == m:
    #                 break
    #             max_cnt = max(max_cnt, dict_cnt.get(m, 0))
    #         dict_cnt[n] = max_cnt + 1
    #     return max(dict_cnt.values())

    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    result[i] = max(result[i], result[j])
            result[i] += 1
        return max(result)


# leetcode submit region end(Prohibit modification and deletion)
