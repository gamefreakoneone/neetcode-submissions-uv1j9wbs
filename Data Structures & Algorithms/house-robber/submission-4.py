class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        def dfs(house):
            if house >= n:
                return 0
            if house in dp:
                return dp[house]
            
            # Skip this house
            dp[house] = dfs(house+1)

            # or use this house
            dp[house] = max(dp[house] , nums[house] + dfs(house+2))
            return dp[house]
        
        return dfs(0)