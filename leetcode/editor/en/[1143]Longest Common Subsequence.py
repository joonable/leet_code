# Given two strings text1 and text2, return the length of their longest common 
# subsequence. If there is no common subsequence, return 0. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order 
# of the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  A common subsequence of two strings is a subsequence that is common to both 
# strings. 
# 
#  
#  Example 1: 
# 
#  
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#  
# 
#  Example 3: 
# 
#  
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text1.length, text2.length <= 1000 
#  text1 and text2 consist of only lowercase English characters. 
#  
# 
#  Related Topics String Dynamic Programming 👍 14293 👎 219


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 두 문자열의 접두사 조합을 2차원 DP로 비교하면서,
        # 같으면 대각선 +1, 다르면 왼쪽/위쪽 중 큰 값으로 갱신해
        # dp[m][n]에 최장 공통 부분 수열의 길이를 저장한다.
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
