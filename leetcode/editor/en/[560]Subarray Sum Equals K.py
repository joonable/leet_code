# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k. 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics Array Hash Table Prefix Sum 👍 22916 👎 740


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        count_dict = defaultdict(int)
        count_dict[0] = 1
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            result += count_dict[prefix_sum - k]
            count_dict[prefix_sum] += 1
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
