# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one. 
# 
#  You must implement a solution with a linear runtime complexity and use only 
# constant extra space. 
# 
#  
#  Example 1: 
#  Input: nums = [2,2,1]
# Output: 1
#  
#  Example 2: 
#  Input: nums = [4,1,2,1,2]
# Output: 4
#  
#  Example 3: 
#  Input: nums = [1]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  Each element in the array appears twice except for one element which appears 
# only once. 
#  
# 
#  Related Topics Array Bit Manipulation 👍 15594 👎 641


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

    # def singleNumber_dict(self, nums: list[int]) -> int:
    #     d = dict()
    #     for n in nums:
    #         cnt = d.get(n, True)
    #         if cnt:
    #             d[n] = False
    #         else:
    #             del d[n]
    #     single_num = list(d.keys())[0]
    #     return single_num

    # def singleNumber(self, nums: list[int]) -> int:
    #     """
    #     Success:
    #         Runtime:135 ms, faster than 25.12% of Python3 online submissions.
    #         Memory Usage:19 MB, less than 52.67% of Python3 online submissions.
    #     """
    #     d = {n: 0 for n in nums}
    #     for n in nums:
    #         d[n] += 1
    #     for k, v in d.items():
    #         if v == 1:
    #             return k


    # def singleNumber(self, nums: list[int]) -> int:
    #     """
    #     Success:
    #         Runtime:134 ms, faster than 26.73% of Python3 online submissions.
    #         Memory Usage:19.5 MB, less than 8.12% of Python3 online submissions.
    #     """
    #     return 2 * sum(set(nums)) - sum(nums)
# leetcode submit region end(Prohibit modification and deletion)
