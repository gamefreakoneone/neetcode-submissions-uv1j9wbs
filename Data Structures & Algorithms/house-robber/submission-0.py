class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp= [-1]*n

        def rob(i):
            if i >= n: # We are out of houses
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            dp[i] = max(nums[i]+ rob(i+2) , rob(i+1))
            return dp[i]
        
        return rob(0)