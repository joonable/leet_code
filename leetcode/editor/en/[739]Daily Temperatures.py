# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the iᵗʰ day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead. 
# 
#  
#  Example 1: 
#  Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#  
#  Example 2: 
#  Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#  
#  Example 3: 
#  Input: temperatures = [30,60,90]
# Output: [1,1,0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= temperatures.length <= 10⁵ 
#  30 <= temperatures[i] <= 100 
#  
# 
#  Related Topics Array Stack Monotonic Stack 👍 13751 👎 346


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        왜 decreasing?
	    stack에는 크기 기준으로 내림차순이 쌓여야, 현재 값이 더 크면, 쌓아둔 작은 애들을 pop하며 계산할 수 있음
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for idx in range(n):
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev_idx = stack.pop()
                answer[prev_idx] = idx - prev_idx
            stack.append(idx)

        return answer
        
# leetcode submit region end(Prohibit modification and deletion)
