# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position 
# right, and return the reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [5], left = 1, right = 1
# Output: [5]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# Follow up: Could you do it in one pass?
# 
#  Related Topics Linked List 👍 11999 👎 676


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # TODO
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        predecessor = dummy

        for _ in range(left - 1):
            predecessor = predecessor.next

        successor = current = predecessor.next
        prev = None

        for _ in range(right - left + 1):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        predecessor.next = prev
        successor.next = current

        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
