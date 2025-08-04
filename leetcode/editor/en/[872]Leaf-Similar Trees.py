# Consider all the leaves of a binary tree, from left to right order, the 
# values of those leaves form a leaf value sequence. 
# 
#  
# 
#  For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
#  8). 
# 
#  Two binary trees are considered leaf-similar if their leaf value sequence is 
# the same. 
# 
#  Return true if and only if the two given trees with head nodes root1 and 
# root2 are leaf-similar. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,
# null,null,null,null,null,9,8]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each tree will be in the range [1, 200]. 
#  Both of the given trees will have values in the range [0, 200]. 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 4023 👎 104


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TODO yield로 generator를 활용하면 더 좋음
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        yield: 값을 하나씩 계산하며 반환하고 싶을 때 -> 함수의 실행을 일시 중단하고, 값을 하나 반환
        yield from: 다른 제너레이터(또는 iterable) 안에 있는 값을 반복해서 출력하고 싶을 때 -> 하위 iterable 또는 제너레이터를 반복하며 yield 위임


        """
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
                # yield 를 쓸경우 generator 객체 자체를 반환
        return list(dfs(root1)) == list(dfs(root2))


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result1 = list()
        result2 = list()

        def dfs(node, result):
            if node:
                if not node.left and not node.right:
                    result.append(node.val)
                    return

                dfs(node.left, result)
                dfs(node.right, result)

        dfs(root1, result1)
        dfs(root2, result2)
        return result1 == result2
# leetcode submit region end(Prohibit modification and deletion)
