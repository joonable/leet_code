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
from collections import defaultdict, Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ######## dict
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        return [d[0] for d in freqs[:k]]

        ######## dict + bucket
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            bucket[freq].append(num)

        result = []
        for nums in reversed(bucket):
            result.extend(nums)
            if k <= len(result):
                break
        return result

        ######## dict + min_heapq
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        heap = []  # min-heap: (frequency, number)
        for num, freq in freqs.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)  # 최소 빈도 pop

        return [num for freq, num in heap]

        ######## dict + max_heapq
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        heap = []
        for num, freq in freqs.items():
            heappush(heap, (-freq, num))

        result = []
        while len(result) < k:
            freq, num = heappop(heap)
            result.append(num)
        return result

        # ######## counter
        counter = Counter(nums)
        return [tup[0] for tup in counter.most_common(k)]

# leetcode submit region end(Prohibit modification and deletion)
