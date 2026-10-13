class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = {}
        

        def search(i , flag):
            if i >= len(nums) or (flag and i==len(nums)- 1): # We have crossed the ciorcular housing or we are at the last house and checking if the first house has been stolen or not
                return 0

            if (i, flag) in dp:
                return dp[(i,flag)]

            dp[(i, flag)] = max(search(i+1 , flag) , nums[i] + search(i+2 , flag))
            return dp[(i, flag)]

        return max(search( 0, True) , search(1 , False))