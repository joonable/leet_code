# Given an integer array nums, design an algorithm to randomly shuffle the 
# array. All permutations of the array should be equally likely as a result of the 
# shuffling. 
# 
#  Implement the Solution class: 
# 
#  
#  Solution(int[] nums) Initializes the object with the integer array nums. 
#  int[] reset() Resets the array to its original configuration and returns it. 
# 
#  int[] shuffle() Returns a random shuffling of the array. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
# 
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
#                        // Any permutation of [1,2,3] must be equally likely 
# to be returned.
#                        // Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration 
# [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. 
# Example: return [1, 3, 2]
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 50 
#  -10⁶ <= nums[i] <= 10⁶ 
#  All the elements of nums are unique. 
#  At most 10⁴ calls in total will be made to reset and shuffle. 
#  
# 
#  Related Topics Array Math Design Randomized 👍 1384 👎 941


# leetcode submit region begin(Prohibit modification and deletion)
import random
from typing import List

class Solution:
    """
    즉, shuffle() 함수 하나하나는 랜덤이지만,
    많은 시행을 반복했을 때, 셔플 결과(=순열)가 동일한 확률로 나오는 분포를 따른다면 → uniform distribution
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = self.nums[:]    # important
        self.n = len(self.original)

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        """
        Fisher-Yates Shuffle which gives each permutation an equal chance and it's mathematically uniform.
        1.	첫 번째 숫자 자리에 누구 넣을까?
        → 1, 2, 3 중 랜덤하게 하나 고름 (확률 1/3)
        2.	두 번째 자리에 누구 넣을까?
        → 남은 2개 중에서 랜덤하게 하나 (확률 1/2)
        3.	세 번째 자리엔 남은 거 하나 그냥 넣기!

        모든 조합이 나올 확률이:
        → 1/3 * 1/2 * 1 = 1/6
        → 정확히 6개 조합이니까 모든 경우가 공평하게 나와!
        """

        for i in range(self.n):
            j = random.randint(i, self.n - 1)   # important
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# leetcode submit region end(Prohibit modification and deletion)
