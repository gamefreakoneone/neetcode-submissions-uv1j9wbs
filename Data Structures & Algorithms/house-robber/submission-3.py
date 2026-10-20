class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def search(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]

            # We can either skip this house
            dp[i] = search(i+1)

            # Use this house
            dp[i] = max(nums[i] + search(i+2) , dp[i])

            return dp[i]

        return search(0)