# You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
# order, and two integers m and n, representing the number of elements in nums1 and 
# nums2 respectively. 
# 
#  Merge nums1 and nums2 into a single array sorted in non-decreasing order. 
# 
#  The final sorted array should not be returned by the function, but instead 
# be stored inside the array nums1. To accommodate this, nums1 has a length of m + 
# n, where the first m elements denote the elements that should be merged, and the 
# last n elements are set to 0 and should be ignored. nums2 has a length of n. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming 
# from nums1.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there 
# to ensure the merge result can fit in nums1.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -10⁹ <= nums1[i], nums2[j] <= 10⁹ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(m + n) time? 
# 
#  Related Topics Array Two Pointers Sorting 👍 14354 👎 1817


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        while n:  # nums1를 뒤에서 부터 채우므로 nums1을 가리키는 m은 고려하지 않아도됨
            if m and nums1[m - 1] > nums2[n - 1]:  # m이 남아있고, m이 가리키는 값이 더 클경우
                nums1[idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[idx] = nums2[n - 1]
                n -= 1
            idx -= 1

    def merge_sorting(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Runtime:39 ms, faster than 59.63% of Python3 online submissions.
        Memory Usage:16.6 MB, less than 78.07% of Python3 online submissions.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

# leetcode submit region end(Prohibit modification and deletion)
