# The median is the middle value in an ordered integer list. If the size of the 
# list is even, there is no middle value, and the median is the mean of the two 
# middle values. 
# 
#  
#  For example, for arr = [2,3,4], the median is 3. 
#  For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. 
#  
# 
#  Implement the MedianFinder class: 
# 
#  
#  MedianFinder() initializes the MedianFinder object. 
#  void addNum(int num) adds the integer num from the data stream to the data 
# structure. 
#  double findMedian() returns the median of all elements so far. Answers 
# within 10⁻⁵ of the actual answer will be accepted. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#  
# 
#  
#  Constraints: 
# 
#  
#  -10⁵ <= num <= 10⁵ 
#  There will be at least one element in the data structure before calling 
# findMedian. 
#  At most 5 * 10⁴ calls will be made to addNum and findMedian. 
#  
# 
#  
#  Follow up: 
# 
#  
#  If all integer numbers from the stream are in the range [0, 100], how would 
# you optimize your solution? 
#  If 99% of all integer numbers from the stream are in the range [0, 100], how 
# would you optimize your solution? 
#  
# 
#  Related Topics Two Pointers Design Sorting Heap (Priority Queue) Data Stream 
# 👍 12449 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.max_heap = []  # left side (as max heap) e.g. [-4, -3]
        self.min_heap = []  # right side (as min heap) e.g. [5, 9]

    def addNum(self, num: int) -> None:
        # Step 1: Always push into max_heap first (as negative)
        heappush(self.max_heap, -num)

        # Step 2: Balance → move the largest from max_heap to min_heap
        heappush(self.min_heap, -heappop(self.max_heap))

        # Step 3: Rebalance if min_heap has more elements
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]

# class MedianFinder:

#     def __init__(self):
#         self.max_heap = [] # max_heap[0] is always the MAX in this heap (negtive)
#         self.min_heap = [] # min_heap[0] is always the MIN in this heap
#         self.len_heap = 0

#     def addNum(self, num: int) -> None:
#         if not self.max_heap :
#             heappush(self.max_heap, -num)
#         else:
#             if num > -self.max_heap[0]:
#                 heappush(self.min_heap, num)
#             else:
#                 heappush(self.max_heap, -num)

#             if len(self.max_heap) < len(self.min_heap):
#                 val = heappop(self.min_heap)
#                 heappush(self.max_heap, -val)
#             elif len(self.max_heap) - len(self.min_heap) > 1:
#                 val = heappop(self.max_heap)
#                 heappush(self.min_heap, -val)

#     def findMedian(self) -> float:
#         if len(self.max_heap) == len(self.min_heap):
#             return (-self.max_heap[0] + self.min_heap[0]) / 2
#         else:
#             return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# max_heap = [-3, -2] ->
# min_heap = [1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
