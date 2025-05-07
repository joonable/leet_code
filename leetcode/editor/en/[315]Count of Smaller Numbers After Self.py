# Given an integer array nums, return an integer array counts where counts[i] 
# is the number of smaller elements to the right of nums[i]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,-1]
# Output: [0,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search Divide and Conquer Binary Indexed Tree 
# Segment Tree Merge Sort Ordered Set 👍 9011 👎 247


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        nums = list(enumerate(nums))    # important

        def merge_sort(start, end):
            if end - start <= 1:    # important
                return nums[start:end]  # base case: 하나짜리 배열

            mid = (start + end) // 2
            left_nums = merge_sort(start, mid)
            right_nums = merge_sort(mid, end)

            merged = []
            left_idx = right_idx = 0

            # 병합하면서 count 누적
            while left_idx < len(left_nums) and right_idx < len(right_nums):
                # right[j]가 더 작으면: left[i]보다 먼저 나올 작고 오른쪽에 있는 수
                if left_nums[left_idx][1] <= right_nums[right_idx][1]:
                    # j개 만큼 작은 수가 이미 나온 것 → 카운트 누적
                    result[left_nums[left_idx][0]] += right_idx     # important
                    merged.append(left_nums[left_idx])
                    left_idx += 1
                else:
                    merged.append(right_nums[right_idx])
                    right_idx += 1

            # 남은 left 정리
            while left_idx < len(left_nums):
                result[left_nums[left_idx][0]] += right_idx
                merged.append(left_nums[left_idx])
                left_idx += 1

            # 남은 right 정리 (count 필요 없음)
            while right_idx < len(right_nums):
                merged.append(right_nums[right_idx])
                right_idx += 1

            return merged

        merge_sort(0, n)
        return result
# leetcode submit region end(Prohibit modification and deletion)
