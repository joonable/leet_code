# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted 
# with a number on it represented by an array nums. You are asked to burst all the 
# balloons. 
# 
#  If you burst the iᵗʰ balloon, you will get nums[i - 1] * nums[i] * nums[i + 1
# ] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if 
# there is a balloon with a 1 painted on it. 
# 
#  Return the maximum coins you can collect by bursting the balloons wisely. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167 
# 
#  Example 2: 
# 
#  
# Input: nums = [1,5]
# Output: 10
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  0 <= nums[i] <= 100 
#  
# 
#  Related Topics Array Dynamic Programming 👍 9595 👎 279


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 양쪽에 1을 추가해 경계 안정화
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[i][j]: i와 j 사이의 풍선을 모두 터뜨렸을 때 얻을 수 있는 최대 점수
        # (i, j)는 '경계'이고, 실제 터지는 풍선은 i+1 ~ j-1
        dp = [[0] * n for _ in range(n)]

        # 구간 길이를 2부터 시작 (i, j가 바로 붙으면 사이에 풍선이 없으므로)
        for length in range(2, n):
            # i: 구간의 시작점
            for i in range(0, n - length):
                # j: 구간의 끝점
                j = i + length

                # (i, j) 구간 안에서 마지막으로 터뜨릴 풍선 k를 하나씩 시도
                for k in range(i + 1, j):
                    # 왼쪽 구간: (i, k)
                    # 오른쪽 구간: (k, j)
                    # 마지막으로 k를 터뜨릴 때 점수: nums[i]*nums[k]*nums[j]
                    # 사이에 풍선은 이미 터졌으므로 k-1, k+1이 아님
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    )

        # dp[0][n-1]: 전체 구간 (가장 왼쪽~가장 오른쪽) 풍선을 모두 터뜨릴 때 최대 점수
        return dp[0][-1]
# leetcode submit region end(Prohibit modification and deletion)
