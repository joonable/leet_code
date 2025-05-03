# Given an unsorted integer array nums. Return the smallest positive integer 
# that is not present in nums. 
# 
#  You must implement an algorithm that runs in O(n) time and uses O(1) 
# auxiliary space. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  Related Topics Array Hash Table 👍 17486 👎 1917


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: 각 숫자를 자신의 위치 (val -> index val-1)로 이동
        for i in range(n):
            correct_index = nums[i] - 1  # important
            while 1 <= nums[i] <= n \
                    and nums[correct_index] != nums[i]:  # important
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Step 2: 첫 번째로 불일치하는 index를 찾기 → 그 자리에 있어야 할 숫자가 없음
        for i, num in enumerate(nums):
            correct_num = i + 1
            if num != correct_num:  # important
                return correct_num  # 이 자리에 있어야 할 숫자가 없는 것

        # Step 3: 모든 자리에 알맞은 숫자가 있을 경우 → 다음 숫자가 빠짐
        return n + 1

# leetcode submit region end(Prohibit modification and deletion)
