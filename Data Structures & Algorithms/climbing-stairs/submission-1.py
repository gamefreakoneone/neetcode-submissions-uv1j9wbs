class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i >= n:
                return i==n
            
            if i in dp:
                return dp[i]

            # We can take 1 step or 2. We are counting number of distinct ways so addition is lright
            dp[i] = dfs(i+1) + dfs(i+2)

            return dp[i]

        return dfs(0)