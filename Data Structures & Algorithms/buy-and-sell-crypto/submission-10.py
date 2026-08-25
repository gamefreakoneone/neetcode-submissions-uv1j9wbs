class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_P = -float('inf')
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            profit = price - lowest_price
            if profit > max_P:
                max_P = profit

        return max_P
        