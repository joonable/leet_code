# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the 
# node's key. 
#  The right subtree of a node contains only nodes with keys greater than the 
# node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 1746
# 6 👎 1402


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, -float('inf'), float('inf'))
        
# leetcode submit region end(Prohibit modification and deletion)
