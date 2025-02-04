# Given the root of a Binary Search Tree (BST), return the minimum absolute 
# difference between the values of any two different nodes in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/ 
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search 
# Tree Binary Tree 👍 4516 👎 242


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev_val = float("inf")

        def get_min_diff(node):
            if not node:
                return

            get_min_diff(node.left)
            self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
            self.prev_val = node.val
            get_min_diff(node.right)

        get_min_diff(root)
        return self.min_diff
# leetcode submit region end(Prohibit modification and deletion)
