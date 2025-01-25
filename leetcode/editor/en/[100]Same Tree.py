# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
#  
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
#  
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 11
# 940 👎 256


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional
# Definition for a binary tree node.
# TODO
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
# leetcode submit region end(Prohibit modification and deletion)