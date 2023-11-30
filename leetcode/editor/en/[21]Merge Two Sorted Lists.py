# You are given the heads of two sorted linked lists list1 and list2. 
# 
#  Merge the two lists in a one sorted list. The list should be made by 
# splicing together the nodes of the first two lists. 
# 
#  Return the head of the merged linked list. 
# 
#  
#  Example 1: 
#  
#  
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = [], list2 = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both lists is in the range [0, 50]. 
#  -100 <= Node.val <= 100 
#  Both list1 and list2 are sorted in non-decreasing order. 
#  
# 
#  Related Topics Linked List Recursion 👍 16692 👎 1487


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()
        if not (list1 or list2):
            return list2
        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val <= list2.val:
                result.next = ListNode(list1.val)
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next
            result = result.next

        while list1:
            result.next = ListNode(list1.val)
            list1 = list1.next
            result = result.next

        while list2:
            result.next = ListNode(list2.val)
            list2 = list2.next
            result = result.next

        return dummy.next


#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         result_list = temp_list = ListNode()
#         while list1 or list2:
#             if list1 is None:
#                 temp_list.next = list2
#                 break
#             if list2 is None:
#                 temp_list.next = list1
#                 break
#
#             if list1.val < list2.val:
#                 temp_list.next = list1
#                 list1 = list1.next
#             elif list1.val >= list2.val:
#                 temp_list.next = list2
#                 list2 = list2.next
#
#             temp_list = temp_list.next
#         return result_list.next
# # leetcode submit region end(Prohibit modification and deletion)
