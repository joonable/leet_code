# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).
#  
# 
#  Find two lines that together with the x-axis form a container, such that the 
# container contains the most water. 
# 
#  Return the maximum amount of water a container can store. 
# 
#  Notice that you may not slant the container. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can 
# contain is 49.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [1,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  2 <= n <= 10⁵ 
#  0 <= height[i] <= 10⁴ 
#  
# 
#  Related Topics Array Two Pointers Greedy 👍 30942 👎 1965


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            result = max(result, width * min_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        left, right = 0, n - 1

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
# leetcode submit region end(Prohibit modification and deletion)
