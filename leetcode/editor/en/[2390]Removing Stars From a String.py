# You are given a string s, which contains stars *. 
# 
#  In one operation, you can: 
# 
#  
#  Choose a star in s. 
#  Remove the closest non-star character to its left, as well as remove the 
# star itself. 
#  
# 
#  Return the string after all stars have been removed. 
# 
#  Note: 
# 
#  
#  The input will be generated such that the operation is always possible. 
#  It can be shown that the resulting string will always be unique. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1ˢᵗ star is 't' in "leet**cod*e". s becomes 
# "lee*cod*e".
# - The closest character to the 2ⁿᵈ star is 'e' in "lee*cod*e". s becomes 
# "lecod*e".
# - The closest character to the 3ʳᵈ star is 'd' in "lecod*e". s becomes 
# "lecoe".
# There are no more stars, so we return "lecoe". 
# 
#  Example 2: 
# 
#  
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of lowercase English letters and stars *. 
#  The operation above can be performed on s. 
#  
# 
#  Related Topics String Stack Simulation 👍 2743 👎 190


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == "*":
                result.pop()
            else:
                result.append(ch)
        return "".join(result)


    def removeStars(self, s: str) -> str:
        """
        Runtime:139 ms, faster than 61.42% of Python3 online submissions.
        Memory Usage:18.7 MB, less than 49.22% of Python3 online submissions.
        """
        from collections import deque
        dq = deque()
        for ch in s:
            if ch == "*":
                dq.pop()
            else:
                dq.append(ch)
        if dq:
            return "".join([dq.popleft() for _ in range(len(dq))])
        else:
            return ""
        # """
        # Runtime:194 ms, faster than 31.62% of Python3 online submissions.
        # Memory Usage:18.6 MB, less than 49.22% of Python3 online submissions.
        # """
        # result = ["" for _ in range(len(s))]
        # pos = 0
        # for ch in s:
        #     if ch != "*":
        #         result[pos] = ch
        #         pos += 1
        #     else:
        #         pos -= 1
        # return "".join(result[:pos])
        #


# leetcode submit region end(Prohibit modification and deletion)
