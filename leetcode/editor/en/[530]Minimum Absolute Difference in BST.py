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
# TODO 인접의 정의가 헷갈림. 4 <-> 2 비교 않고 4 <-> 3 비교해야함. BST를 좀 더 이해해야할듯
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
        self.prev_val = float("inf")    # TODO (상위가 아닌) 하위 노드를 저장

        # TODO 제일 먼저 왼쪽 최하위까지 내려간후 다시 올라옴
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
            self.prev_val = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
# leetcode submit region end(Prohibit modification and deletion)
