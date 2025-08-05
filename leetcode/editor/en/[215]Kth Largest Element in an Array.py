# Given an integer array nums and an integer k, return the kᵗʰ largest element 
# in the array. 
# 
#  Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ 
# distinct element. 
# 
#  Can you solve it without sorting? 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#  
#  Example 2: 
#  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#  
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Divide and Conquer Sorting Heap (Priority Queue) 
# Quickselect 👍 17786 👎 931


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for num in nums[k:]:
            if heap[0] < num:
                heappush(heap, num)
                heappop(heap)
        return heap[0]
        
# leetcode submit region end(Prohibit modification and deletion)
