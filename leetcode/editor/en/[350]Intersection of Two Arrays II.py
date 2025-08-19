# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must appear as many times as it shows in both 
# arrays and you may return the result in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
# 
#  
#  Follow up: 
# 
#  
#  What if the given array is already sorted? How would you optimize your 
# algorithm? 
#  What if nums1's size is small compared to nums2's size? Which algorithm is 
# better? 
#  What if elements of nums2 are stored on disk, and the memory is limited such 
# that you cannot load all elements into the memory at once? 
#  
# 
#  Related Topics Array Hash Table Two Pointers Binary Search Sorting 👍 6935 👎
#  914


# leetcode submit region begin(Prohibit modification and deletion)

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        result = []
        for num in nums2:
            if num in nums1_counter:
                if nums1_counter[num] > 0:
                    result.append(num)
                nums1_counter[num] -= 1
        return result

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Runtime:58 ms, faster than 34.85% of Python3 online submissions.
        Memory Usage:16.4 MB, less than 32.58% of Python3 online submissions.
        """
        # d_cnt = dict()
        # nums1.sort(), nums2.sort()
        # pos1, pos2 = 0, 0
        # len1, len2 = len(nums1), len(nums2)
        # while True:
        #     v1, v2 = nums1[pos1], nums2[pos2]
        #     if v1 == v2:
        #         d_cnt[v1] = d_cnt.get(v1, 0) + 1
        #         pos1 += 1
        #         pos2 += 1
        #     elif v1 < v2:
        #         pos1 += 1
        #     elif v1 > v2:
        #         pos2 += 1
        #     if pos1 >= len1 or pos2 >= len2:
        #         break
        #
        # list_result = [[v] * cnt for v, cnt in d_cnt.items()]
        #
        # from itertools import chain
        # list_result = [x for x in chain(*list_result)]
        #
        # return list_result

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Runtime:48 ms, faster than 83.79% of Python3 online submissions.
        Memory Usage:16.4 MB, less than 65.21% of Python3 online submissions.
        """
        list_result = list()

        cnt_nums1 = Counter(nums1)
        del nums1

        cnt_nums2 = Counter(nums2)
        del nums2

        for k in set(list(cnt_nums1.keys()) + list(cnt_nums2.keys())):
            v1 = cnt_nums1.get(k, 0)
            v2 = cnt_nums2.get(k, 0)
            list_result.extend([k] * min(v1, v2))
        return list_result
