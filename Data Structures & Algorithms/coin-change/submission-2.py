class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = {}

        def dfs(i, currSum):
            if i == len(coins) or currSum > amount:
                return float('inf')
            
            if currSum == amount:
                return 0 # Since we we have reached the target

            if (i, currSum) in dp:
                return dp[(i, currSum)]

            skip = dfs(i+1 , currSum)
            take = coins[i] + currSum

            dp[(i,currSum)] = min(1 + dfs(i , take) , skip)

            return dp[(i,currSum)]

        return dp[(0,0)] if dfs(0,0) != float('inf') else -1 