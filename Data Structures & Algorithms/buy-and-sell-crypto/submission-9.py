class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0
        for p in prices:
            if p < lowest:
                lowest = p
            profit = p - lowest
            max_profit = max(profit, max_profit)
        return max_profit