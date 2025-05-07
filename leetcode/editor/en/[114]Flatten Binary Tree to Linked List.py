# Given the root of a binary tree, flatten the tree into a "linked list": 
# 
#  
#  The "linked list" should use the same TreeNode class where the right child 
# pointer points to the next node in the list and the left child pointer is always 
# null. 
#  The "linked list" should be in the same order as a pre-order traversal of 
# the binary tree. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Can you flatten the tree in-place (with 
# O(1) extra space)?
# 
#  Related Topics Linked List Stack Tree Depth-First Search Binary Tree 👍 12694
#  👎 572


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    def flatten_iterative(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if stack:
                node.right = stack[-1]
            node.left = None

    def flatten_dfs(self, root: Optional[TreeNode]) -> None:
        prev = None  # 마지막으로 방문한 노드를 추적

        def dfs(node):
            nonlocal prev
            if not node:
                return

            # 오른쪽부터 탐색해야 prev를 올바르게 연결할 수 있음 (preorder + 역순)
            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node

        dfs(root)

    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     while root:
    #         if root.left:
    #             left_node = root.left
    #             while left_node.right:
    #                 left_node = left_node.right
    #             left_node.right = root.right
    #             root.right = root.left
    #             root.left = None
    #         root = root.right

# leetcode submit region end(Prohibit modification and deletion)
