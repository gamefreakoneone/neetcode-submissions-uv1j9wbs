class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currPrice = prices[0]

        for price in prices:
            profit = price - currPrice
            maxProfit = max(profit, maxProfit)
            currPrice = min(price , currPrice)

        return maxProfit