# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics Array Two Pointers Dynamic Programming Stack Monotonic Stack ?
# ? 33836 👎 591


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap_stack(self, height: List[int]) -> int:
        stack = []
        total_water = 0

        for i, h in enumerate(height):
            # 현재 높이가 스택 위보다 크면 물이 고일 수 있음
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()

                if not stack:
                    break  # 왼쪽 벽이 없으면 고일 수 없음

                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], h) - height[bottom]
                total_water += width * bounded_height

            stack.append(i)

        return total_water

    def trap(self, height: List[int]) -> int:
        """
        ✅ One-line summary
        We move from both ends to the center,
        and always calculate trapped water at the lower wall side.

        🔍 3 Key Points (Simple English)
            1.	Water can only be trapped if there are taller walls on both sides.
            2.	At each step, we look at which side is lower, and move that side.
            3.	We keep track of the highest wall seen so far, and trap water based on the difference.
        """
        # if not height or len(height) < 3:
        #     return 0

        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                # 왼쪽이 더 낮으면 왼쪽을 기준으로 물 계산
                if height[left] >= left_max: # important
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # 오른쪽이 더 낮으면 오른쪽을 기준으로 물 계산
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
# leetcode submit region end(Prohibit modification and deletion)
