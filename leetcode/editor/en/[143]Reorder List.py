# You are given the head of a singly linked-list. The list can be represented 
# as: 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  Reorder the list to be on the following form: 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#  
# 
#  You may not modify the values in the list's nodes. Only nodes themselves may 
# be changed. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 5 * 10⁴]. 
#  1 <= Node.val <= 1000 
#  
# 
#  Related Topics Linked List Two Pointers Stack Recursion 👍 11672 👎 447


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None  # important

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while second:  # important
            next_first_node = first.next
            next_second_node = second.next

            first.next = second
            second.next = next_first_node

            first = next_first_node
            second = next_second_node

        return head
        
# leetcode submit region end(Prohibit modification and deletion)
