class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0
        # min_price = prices[0]
        # max_profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     elif prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price
        # return max_profit
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit