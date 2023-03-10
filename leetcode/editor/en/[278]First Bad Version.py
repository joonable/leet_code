# You are a product manager and currently leading a team to develop a new 
# product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions 
# after a bad version are also bad. 
# 
#  Suppose you have n versions [1, 2, ..., n] and you want to find out the 
# first bad one, which causes all the following ones to be bad. 
# 
#  You are given an API bool isBadVersion(version) which returns whether 
# version is bad. Implement a function to find the first bad version. You should 
# minimize the number of calls to the API. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, bad = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= bad <= n <= 2³¹ - 1 
#  
# 
#  Related Topics Binary Search Interactive 👍 6652 👎 2562


# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1

        def binary_search(left_pos, right_pos):
            pivot_idx = (left_pos + right_pos) // 2
            is_bad_prev = isBadVersion(pivot_idx - 1)
            is_bad = isBadVersion(pivot_idx)

            if is_bad_prev is False and is_bad is False:
                return binary_search(pivot_idx, right_pos)
            elif is_bad_prev and is_bad:
                return binary_search(left_pos, pivot_idx)
            else:
                return pivot_idx

        return binary_search(1, n+1)



