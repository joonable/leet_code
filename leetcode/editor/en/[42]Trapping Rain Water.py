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
    def trap_monotonic_stack(self, height: List[int]) -> int:
        stack = []
        total = 0
        for right, right_height in enumerate(height):
            # 물을 채울수 있는 조건: 현재 벽이 더 높은 벽일 때만 빗물을 채울 수 있음
            # Increasing: stack에 값을 decreasing 하게 모으다가 더 큰 값 출현 시 이벤트 발생
            while stack and height[stack[-1]] < right_height:
                bottom = stack.pop()
                bottom_height = height[bottom]

                if not stack:  # 왼쪽벽 없으면 물이 못참
                    continue
                left = stack[-1]  # 왼쪽벽
                left_height = height[left]

                bounded_height = min(right_height, left_height) - bottom_height
                width = right - left - 1
                total += bounded_height * width
            stack.append(right)
        return total

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
