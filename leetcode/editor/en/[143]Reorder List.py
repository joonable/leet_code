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

        curr = slow.next    # important 반으로 나누는게 아님 무조건 second가 짧게
        slow.next = None  # important
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # first = 0->1->4 second = 3
        first = head
        second = prev
        while second:
            first_next = first.next  # (1 -> 4)
            second_next = second.next  # None

            first.next = second  # 0 -> 3
            second.next = first_next  # 0 -> 3 -> (1 -> 4)

            second = second_next  # None
            first = first_next  # (1 -> 4)

        return head
        
# leetcode submit region end(Prohibit modification and deletion)
