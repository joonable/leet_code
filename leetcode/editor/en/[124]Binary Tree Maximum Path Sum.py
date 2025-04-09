# A path in a binary tree is a sequence of nodes where each pair of adjacent 
# nodes in the sequence has an edge connecting them. A node can only appear in the 
# sequence at most once. Note that the path does not need to pass through the root. 
# 
# 
#  The path sum of a path is the sum of the node's values in the path. 
# 
#  Given the root of a binary tree, return the maximum path sum of any non-
# empty path. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# 
#  
# 
#  Example 2: 
#  
#  
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 
# = 42.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Dynamic Programming Tree Depth-First Search Binary Tree 👍 174
# 24 👎 762


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            root_sum = left_sum + right_sum + node.val

            max_sum = max(max_sum, root_sum)
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return max_sum
# leetcode submit region end(Prohibit modification and deletion)
