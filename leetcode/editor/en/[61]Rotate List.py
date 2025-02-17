# Given the head of a linked list, rotate the list to the right by k places. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 500]. 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 10⁹ 
#  
# 
#  Related Topics Linked List Two Pointers 👍 10159 👎 1490


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head
        len_list = 0
        while dummy:
            len_list += 1
            dummy = dummy.next

        k %= len_list

        fast = slow = head

        if k == 0:
            return head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        result = slow.next
        slow.next = None
        fast.next = head

        return result


# leetcode submit region end(Prohibit modification and deletion)
