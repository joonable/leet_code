# You are given an array of k linked-lists lists, each linked-list is sorted in 
# ascending order. 
# 
#  Merge all the linked-lists into one sorted linked-list and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#  
# 
#  Example 2: 
# 
#  
# Input: lists = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: lists = [[]]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  k == lists.length 
#  0 <= k <= 10⁴ 
#  0 <= lists[i].length <= 500 
#  -10⁴ <= lists[i][j] <= 10⁴ 
#  lists[i] is sorted in ascending order. 
#  The sum of lists[i].length will not exceed 10⁴. 
#  
# 
#  Related Topics Linked List Divide and Conquer Heap (Priority Queue) Merge 
# Sort 👍 18620 👎 674


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            if head:    # important
                heap.append((head.val, i, head))    # important
        heapify(heap)

        dummy = curr = ListNode()
        while heap:
            _, i, node = heappop(heap)
            curr.next = node
            node = node.next    # important
            curr = curr.next
            if node:    # important
                heappush(heap, (node.val, i, node))

        return dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     from queue import PriorityQueue
    #     pq = PriorityQueue()
    #     ptr_dummy = ListNode(0)
    #     ptr_curr = ptr_dummy
    #
    #     for i, lst in enumerate(lists):
    #         while lst:
    #             pq.put((lst.val))
    #             lst = lst.next
    #
    #     while not pq.empty():
    #         ptr_curr.next = ListNode(pq.get())
    #         ptr_curr = ptr_curr.next
    #     return ptr_dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     len_lists = len(lists)
    #     if len_lists == 0:
    #         return
    #     elif len_lists == 1 and lists[0] is None:
    #         return
    #
    #     ptr_dummy = ListNode(0)
    #     ptr_curr = ptr_dummy
    #
    #     while True:
    #         min_idx = -1
    #         min_val = 10 ** 4 + 1
    #         for i in range(len_lists):
    #             if lists[i]:
    #                 if min_val > lists[i].val:
    #                     min_val = lists[i].val
    #                     min_idx = i
    #
    #         if min_idx == -1:
    #             return ptr_dummy.next
    #         else:
    #             lists[min_idx] = lists[min_idx].next
    #             ptr_curr.next = ListNode(min_val)
    #             ptr_curr = ptr_curr.next
    #         # return ptr_curr

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     len_lists = len(lists)
    #     if len_lists == 0:
    #         return
    #     elif len_lists == 1 and lists[0] is None:
    #         return
    #
    #     ptr_dummy = ListNode(0)
    #     ptr_curr = ptr_dummy
    #
    #     while True:
    #         min_idx = -1
    #         min_val = 10 ** 4 + 1
    #         for i in range(len_lists):
    #             if lists[i]:
    #                 if min_val > lists[i].val:
    #                     min_val = lists[i].val
    #                     min_idx = i
    #
    #         if min_idx == -1:
    #             return ptr_dummy.next
    #         else:
    #             lists[min_idx] = lists[min_idx].next
    #             ptr_curr.next = ListNode(min_val)
    #             ptr_curr = ptr_curr.next



# leetcode submit region end(Prohibit modification and deletion)
