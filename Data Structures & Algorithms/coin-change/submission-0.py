class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M,N = len(coins) , amount
        cache = [[None]  * (N+1)  for _ in range(M)]

        def dfs(i, coins, amount, cache):
            if amount == 0:
                return 0
            
            if i == len(coins):
                return float('inf')

            if cache[i][amount] != None:
                return cache[i][amount]

            # We skip the current coin
            cache[i][amount] = dfs(i+1 , coins, amount, cache)

            # We are using the current coin
            left_amount = amount - coins[i]
            if left_amount >= 0:
                count_coins = 1 + dfs(i , coins, left_amount, cache)
                cache[i][amount] = min(count_coins , cache[i][amount])
            
            return cache[i][amount]
        result =dfs(0 , coins, amount, cache) 
        return  result if result != float('inf') else -1