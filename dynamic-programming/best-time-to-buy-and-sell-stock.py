class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for price in prices:
            min_buy = min(min_buy, price)
            profit = max(price - min_buy, profit)
        return max(profit, 0)
