# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the same 
# tree, construct and return the binary tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
# 
#  Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 8330 ?
# ? 140


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_idx = len(inorder) - 1
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            if left > right:
                return None

            nonlocal post_idx
            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)
            root_idx = inorder_idx[root_val]
            root.right = dfs(root_idx + 1, right)
            root.left = dfs(left, root_idx - 1)
            return root

        return dfs(0, len(inorder) - 1)
        
# leetcode submit region end(Prohibit modification and deletion)
