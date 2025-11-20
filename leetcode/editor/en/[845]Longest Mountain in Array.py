# You may recall that an array arr is a mountain array if and only if: 
# 
#  
#  arr.length >= 3 
#  There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that: 
# 
#  
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 
#  
#  
# 
#  Given an integer array arr, return the length of the longest subarray, which 
# is a mountain. Return 0 if there is no mountain subarray. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10⁴ 
#  0 <= arr[i] <= 10⁴ 
#  
# 
#  
#  Follow up: 
# 
#  
#  Can you solve it using only one pass? 
#  Can you solve it in O(1) space? 
#  
# 
#  Related Topics Array Two Pointers Dynamic Programming Enumeration 👍 2978 👎 
# 90


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        up = [0] * n
        down = [0] * n

        # 1) 왼쪽 → 오른쪽 증가 dp
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        # 2) 오른쪽 → 왼쪽 감소 dp
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1

        # 3) peak를 중심으로 mountain 길이 계산
        best = 0
        for i in range(1, n - 1):
            if up[i] > 0 and down[i] > 0:
                best = max(best, up[i] + down[i] + 1)

        return best
        
# leetcode submit region end(Prohibit modification and deletion)
