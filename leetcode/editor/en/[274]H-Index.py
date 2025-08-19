# Given an array of integers citations where citations[i] is the number of 
# citations a researcher received for their iᵗʰ paper, return the researcher's h-index.
#  
# 
#  According to the definition of h-index on Wikipedia: The h-index is defined 
# as the maximum value of h such that the given researcher has published at least 
# h papers that have each been cited at least h times. 
# 
#  
#  Example 1: 
# 
#  
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each 
# of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the 
# remaining two with no more than 3 citations each, their h-index is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: citations = [1,3,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == citations.length 
#  1 <= n <= 5000 
#  0 <= citations[i] <= 1000 
#  
# 
#  Related Topics Array Sorting Counting Sort 👍 1149 👎 498

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter
from operator import itemgetter
from itertools import accumulate

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        for citation in citations:
            if citation >= n:
                count[n + 1] += 1
            else:
                count[citation] += 1

        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0

    def hIndex_sort(self, citations: List[int]) -> int:
        citations.sort()
        # [0,1,3,5,6]
        n_papers = len(citations)
        h_index = 0
        for idx, citation in enumerate(citations):
            h_index = max(h_index, min(n_papers - idx, citation))
        return h_index

    def hIndex_sort_v2(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(key=lambda x: -x)
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                pass
            else:
                return i
        return n
# leetcode submit region end(Prohibit modification and deletion)
