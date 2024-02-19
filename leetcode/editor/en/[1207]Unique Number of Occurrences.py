# Given an array of integers arr, return true if the number of occurrences of 
# each value in the array is unique or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two 
# values have the same number of occurrences. 
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  -1000 <= arr[i] <= 1000 
#  
# 
#  Related Topics Array Hash Table 👍 4887 👎 124


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    Runtime:30 ms, faster than 97.92% of Python3 online submissions.
    Memory Usage:16.6 MB, less than 96.59% of Python3 online submissions.
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        list_cnt = counter.values()
        dict_cnt = {}
        for cnt in list_cnt:
            if dict_cnt.get(cnt, True):
                dict_cnt[cnt] = False
            else:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
