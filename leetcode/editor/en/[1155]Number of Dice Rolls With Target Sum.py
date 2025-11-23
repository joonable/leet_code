# You have n dice, and each dice has k faces numbered from 1 to k. 
# 
#  Given three integers n, k, and target, return the number of possible ways (
# out of the kⁿ total ways) to roll the dice, so the sum of the face-up numbers 
# equals target. Since the answer may be too large, return it modulo 10⁹ + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 10⁹ + 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n, k <= 30 
#  1 <= target <= 1000 
#  
# 
#  Related Topics Dynamic Programming 👍 5282 👎 185


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[t] = (현재 i개의 주사위로) 합 t를 만드는 방법 수
        dp = [0] * (target + 1)
        dp[0] = 1  # 0개로 합 0 만드는 경우 1개

        for _ in range(n):  # 주사위 1개씩 늘려가기
            new_dp = [0] * (target + 1)
            window_sum = 0  # 슬라이딩 윈도우 합

            for t in range(1, target + 1):
                # window 오른쪽 추가: dp[t-1]
                window_sum += dp[t - 1]

                # window 왼쪽 제거: dp[t-k-1]
                if t - k - 1 >= 0:
                    window_sum -= dp[t - k - 1]

                new_dp[t] = window_sum % MOD

            dp = new_dp

        return dp[target]

    def numRollsToTarget_dp(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i][t] = i개의 주사위로 합 t를 만드는 방법 수
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 0개로 합 0 만드는 경우 1개

        for i in range(1, n + 1):  # i개의 주사위
            for t in range(1, min(i * k, target) + 1):  # 가능한 합 범위
                for j in range(1, min(k, t) + 1):  # 이번 주사위 눈(1~k)
                    dp[i][t] = (dp[i][t] + dp[i - 1][t - j]) % MOD

        return dp[n][target]
# leetcode submit region end(Prohibit modification and deletion)
