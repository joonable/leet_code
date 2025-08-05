# Given a linked list, swap every two adjacent nodes and return its head. You 
# must solve the problem without modifying the values in the list's nodes (i.e., 
# only nodes themselves may be changed.) 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics Linked List Recursion 👍 11424 👎 418


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:  # TODO
            first = curr.next
            second = curr.next.next

            next_node = second.next
            curr.next = second
            curr = curr.next
            curr.next = first
            curr = curr.next
            curr.next = next_node

        return dummy.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        ptr_dummy = ListNode(0)
        ptr_curr = ptr_dummy
        is_even = False
        temp_val = 0

        while True:
            if not is_even:
                temp_val = head.val
                is_even = True
            else:
                ptr_curr.next = ListNode(head.val)
                ptr_curr = ptr_curr.next
                ptr_curr.next = ListNode(temp_val)
                ptr_curr = ptr_curr.next
                is_even = False
            head = head.next
            if not head:
                break

        if is_even:
            ptr_curr.next = ListNode(temp_val)

        return ptr_dummy.next




# leetcode submit region end(Prohibit modification and deletion)
