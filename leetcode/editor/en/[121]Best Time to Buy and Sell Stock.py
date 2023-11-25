# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock. 
# 
#  Return the maximum profit you can achieve from this transaction. If you 
# cannot achieve any profit, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you 
# must buy before you sell.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming 👍 22524 👎 711

# [7,1,5,3,6,4] = 5
# [7,1,5,3,10,4] = 9
# [7,3,10,1,6,4] = 7
# [7,3,10,1,6,10] = 9


# 0 4 0 3 0
# 0 4 0 7 0
# 0 7 0 5 0
# 0 7 0 5 4
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for i, price in enumerate(prices[:-1]):
        #     i
        result_min = 10001
        # result_max = 1001
        result_output = -1
        for i, price in enumerate(prices):
            if price <= result_min:
                result_min = price
            if price - result_min > result_output:
                result_output = price - result_min
        return result_output
# leetcode submit region end(Prohibit modification and deletion)
