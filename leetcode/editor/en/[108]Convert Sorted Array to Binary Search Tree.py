# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
#  
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in a strictly increasing order. 
#  
# 
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 11278 👎 590


# leetcode submit region begin(Prohibit modification and deletion)
# from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sorted_array_to_bst(arr):
            len_arr = len(arr)
            if len_arr == 0:
                return None
            mid_idx = len_arr // 2
            # print(arr, mid_idx, arr[mid_idx])
            left_subtree = sorted_array_to_bst(arr[:mid_idx])
            right_subtree = sorted_array_to_bst(arr[mid_idx+1:])
            return TreeNode(arr[mid_idx], left_subtree, right_subtree)
        return sorted_array_to_bst(nums)
# leetcode submit region end(Prohibit modification and deletion)
