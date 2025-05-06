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
'''
Input: heights = [2,1,5,6,2,3] Output: 10
stack = [1(1), 4(2), 5(3)]
c_i:0, c_h:2 -> append
c_i:1, c_h:1 ->  p_i=0, p_h=2, w=1, a=2, m=2
c_i:2, c_h:5 -> append
c_i:3, c_h:6 -> append
c_i:4, c_h:2 -> p_i=3, p_h=6, w=1, a=6, m=6 -> p_i=2, p_h=5, w=2, a=10, m=10
c_i:5, c_h:3 -> append
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        왜 “Increasing Stack”이냐?
	    •	우리는 “현재 바보다 높은 바들이 어디까지 계속 있었는지” 추적해야 .
	    •	만약 현재 바가 낮아지면, 이전 바들을 기준으로 직사각형을 만들어볼 수 있는 시점
	    •	그래서 stack에는 height가 증가하는 인덱스만 쌓음
        """
        stack = []
        max_area = 0
        heights.append(0) # important
        for curr_index, curr_height in enumerate(heights):
            while stack and heights[stack[-1]] > curr_height: # important
                prev_index = stack.pop()
                prev_height = heights[prev_index]
                width = curr_index if not stack else curr_index - stack[-1] - 1 # important
                # 스택이 비었을 때는 왼쪽에 아무 벽도 없다는 뜻 (즉, 지금까지 모든 막대들이 다 높거나 같은 애들이었음)
                # → 전체 폭으로 직사각형 만들어도 된다는 뜻
                area = prev_height * width
                max_area = max(area, max_area)
            stack.append(curr_index)
        return max_area

# leetcode submit region end(Prohibit modification and deletion)
