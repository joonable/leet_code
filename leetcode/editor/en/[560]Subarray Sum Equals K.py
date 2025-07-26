# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k. 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics Array Hash Table Prefix Sum 👍 22916 👎 740


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
"""
지금까지의 누적합 curr_sum을 계속 업데이트하면서,
curr_sum - k가 과거에 몇 번 나왔는지 체크
그만큼의 구간이 “합이 k인 부분배열”이라는 뜻!

prefix_counts 구조: 누적합 값 → 그 누적합이 나온 횟수

prefix_counts = {
    0: 1,  # 처음 아무것도 안 더한 상태 (중요한 초기값!)
    1: 1,  # 합이 1인 지점까지 한 번 나옴
    3: 1,  # 합이 3인 지점까지 한 번 나옴 → 여기가 중요!
    6: 1   # 합이 6인 지점까지 한 번 나옴
}
"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_counts = defaultdict(int)    # prefix_counts 와 prefix_sums 는 다름
        prefix_counts[0] = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            result += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
