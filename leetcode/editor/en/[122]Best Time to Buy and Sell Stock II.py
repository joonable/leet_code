

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: # important
                max_profit += prices[i] - prices[i-1]
        return max_profit

    # def maxProfit(self, prices: list[int]) -> int:
    #     profit = 0
    #     current_stock = None
    #     last_day = len(prices)-1
    #     for i in range(1, len(prices)):
    #         print(f"{i} day")
    #         if not current_stock:
    #             if i == last_day:
    #                 print("last no buy")
    #                 break
    #             if prices[i-1] <= prices[i]:
    #                 current_stock = prices[i]
    #                 print("buy")
    #         else:
    #             if i == last_day:
    #                 profit += prices[i+1] - current_stock
    #                 print("last sell")
    #                 break
    #             elif prices[i] > prices[i+1]:
    #                 profit += prices[i] - current_stock
    #                 current_stock = None
    #                 print("sell")
    #
    #     return profit
