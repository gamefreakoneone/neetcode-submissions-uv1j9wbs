class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backTrack(i, currSum):
            if i== len(nums):
                return 1 if currSum == target else 0
            if ( i , currSum) in dp:
                return dp[(i,currSum)]

            dp[(i , currSum)] = backTrack(i+1 , currSum + nums[i]) + backTrack(i+1 , currSum - nums[i])

            return dp[(i , currSum)]

        return backTrack(0 , 0)
        
