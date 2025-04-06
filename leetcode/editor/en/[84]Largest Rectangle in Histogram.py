# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the 
# histogram. 
# 
#  
#  Example 1: 
#  
#  
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#  
# 
#  Example 2: 
#  
#  
# Input: heights = [2,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= heights.length <= 10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  Related Topics Array Stack Monotonic Stack 👍 18082 👎 319


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights = heights + [0]
        for cur_idx in range(len(heights)):
            while stack and heights[stack[-1]] > heights[cur_idx]:
                prev_idx = stack.pop()
                height = heights[prev_idx]
                width = cur_idx - stack[-1] - 1 if stack else cur_idx
                max_area = max(max_area, height * width)
            stack.append(cur_idx)

        return max_area
# leetcode submit region end(Prohibit modification and deletion)
