# Given an integer array arr, return the length of a maximum size turbulent 
# subarray of arr. 
# 
#  A subarray is turbulent if the comparison sign flips between each adjacent 
# pair of elements in the subarray. 
# 
#  More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said 
# to be turbulent if and only if: 
# 
#  
#  For i <= k < j: 
#  
# 
#  
#  arr[k] > arr[k + 1] when k is odd, and 
#  arr[k] < arr[k + 1] when k is even. 
#  
#  
#  Or, for i <= k < j:
#  
#  arr[k] > arr[k + 1] when k is even, and 
#  arr[k] < arr[k + 1] when k is odd. 
#  
#  
# 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [4,8,12,16]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [100]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 4 * 10⁴ 
#  0 <= arr[i] <= 10⁹ 
#  
# 
#  Related Topics Array Dynamic Programming Sliding Window 👍 2089 👎 255


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        max_length = 1
        up_down = 1
        down_up = 1

        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                new_up_down = 1
                new_down_up = up_down + 1
            elif arr[i - 1] > arr[i]:
                new_up_down = down_up + 1
                new_down_up = 1
            else:
                new_up_down = 1
                new_down_up = 1
            up_down, down_up = new_up_down, new_down_up
            max_length = max(max_length, new_up_down, new_down_up)
        return max_length


    # def maxTurbulenceSize(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     if n < 2:
    #         return n

    #     if arr[0] < arr[1]:
    #         prev_op = "<"
    #     elif arr[0] > arr[1]:
    #         prev_op = ">"
    #     else:
    #         prev_op = "="
    #     curr_turbulent = 0 if prev_op == "=" else 1
    #     max_turbulent = curr_turbulent

    #     for i in range(2, n):
    #         if arr[i - 1] < arr[i]:
    #             op = "<"
    #         elif arr[i - 1] > arr[i]:
    #             op = ">"
    #         else:
    #             op = "="

    #         if op == "=":
    #             max_turbulent = max(max_turbulent, curr_turbulent)
    #             curr_turbulent = 0
    #         else:
    #             if prev_op != op:
    #                 curr_turbulent += 1
    #                 max_turbulent = max(max_turbulent, curr_turbulent)
    #             else:
    #                 max_turbulent = max(max_turbulent, curr_turbulent)
    #                 curr_turbulent = 1
    #         prev_op = op

    #     return max_turbulent + 1

# leetcode submit region end(Prohibit modification and deletion)
