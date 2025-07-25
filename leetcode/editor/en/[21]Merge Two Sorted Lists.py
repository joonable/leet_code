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
        dummy = curr = ListNode()  # dummy node

        while list1 and list2:      # important
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # 남은 부분 연결  # important
        curr.next = list1 or list2      # important

        return dummy.next

        # if not list1 and not list2:
        #     return list1
        # elif not list1:
        #     return list2
        # elif not list2:
        #     return list1

        # head = curr = ListNode()

        # while list1 or list2:
        #     if not list1:
        #         curr.next = list2
        #         list2 = list2.next
        #     elif not list2:
        #         curr.next = list1
        #         list1 = list1.next
        #     elif list1.val < list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next

        # return head.next