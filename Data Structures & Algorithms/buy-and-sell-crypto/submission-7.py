class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i , j = 0, 1
        profit = 0
        while i < len(prices) and j < len(prices):
            if prices[i] > prices[j]:
                i = j
            curr_profit=  prices[j] - prices[i]
            if curr_profit > profit :
                profit = curr_profit
            j += 1
        return profit
