# Given the head of a linked list, remove the nᵗʰ node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
# 
#  Related Topics Linked List Two Pointers 👍 17539 👎 730


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr_fast = head
        ptr_slow = head

        for i in range(n):
            ptr_fast = ptr_fast.next
            if not ptr_fast:
                return head.next

        while ptr_fast.next is not None:
            ptr_fast = ptr_fast.next
            ptr_slow = ptr_slow.next

        ptr_slow.next = ptr_slow.next.next

        return head


        # Two pointers - fast and slow
        # slow = head
        # fast = head
        # # Move fast pointer n steps ahead
        # for i in range(0, n):
        #     if fast.next is None:
        #         # If n is equal to the number of nodes, delete the head node
        #         if i == n - 1:
        #             head = head.next
        #         return head
        #     fast = fast.next
        # # Loop until fast node reaches to the end
        # # Now we will move both slow and fast pointers
        # while fast.next is not None:
        #     slow = slow.next
        #     fast = fast.next
        # # Delink the nth node from last
        # if slow.next is not None:
        #     slow.next = slow.next.next
        # return head



# leetcode submit region end(Prohibit modification and deletion)
