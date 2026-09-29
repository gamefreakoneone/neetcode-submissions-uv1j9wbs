class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = {}

        def dfs( i, currSum):
            if i == len(coins) or currSum > amount:
                return float('inf')
            
            if currSum == amount: # Since there are no coins needed to be added
                return 0

            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            # We skip the current coin and move on
            skip = dfs(i+1 , currSum)

            #Or we use the current coin
            newSum = currSum + coins[i]

            dp[(i,currSum)] = min( 1+ dfs(i , newSum) , skip)
            return dp[(i,currSum)]
                        
        result = dfs(0,0)
        print(dp)
        return result if result != float('inf') else -1