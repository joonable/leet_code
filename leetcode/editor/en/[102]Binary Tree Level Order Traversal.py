# Given the root of a binary tree, return the level order traversal of its 
# nodes' values. (i.e., from left to right, level by level). 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Breadth-First Search Binary Tree 👍 16018 👎 344


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
from typing import List, Optional
class Solution:
    def levelOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        def dfs(node, level):
            if not node:
                return
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        result = [result[key] for key in sorted(result.keys())]
        return result


    def level_order_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            result[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [val for key, val in sorted(result.items(), key=lambda x: x[0])]






# leetcode submit region end(Prohibit modification and deletion)
