# Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  
#  Example 2: 
#  Input: nums = [1], k = 1
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  k is in the range [1, the number of unique elements in the array]. 
#  It is guaranteed that the answer is unique. 
#  
# 
#  
#  Follow up: Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size. 
# 
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority 
# Queue) Bucket Sort Counting Quickselect 👍 17979 👎 701


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # return [k for k, v in counter.most_common(k)]

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, cnt in counter.items():
            buckets[cnt].append(num)
        result = []
        for bucket in reversed(buckets):
            result += bucket
            if len(result) == k:
                return result

# leetcode submit region end(Prohibit modification and deletion)
