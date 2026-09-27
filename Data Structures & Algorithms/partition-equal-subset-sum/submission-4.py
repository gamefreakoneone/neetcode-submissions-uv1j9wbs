class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2 != 0:
            return False

        dp ={}

        def dfs( i , currSum):
            if i == len(nums) or currSum > target:
                return 1 if currSum==target else 0
            if currSum==target:
                return 1
            
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            
            # WE skip either the current value
            dp[(i, currSum)] = dfs(i+1 , currSum)
            # print(f"Before pick: ({i}, {currSum} ) : {dp[(i, currSum)]}")
            # or we can pick it up
            newSum = currSum +nums[i]
            dp[(i, currSum)] = max(dfs(i+1 , newSum) , dp[(i,currSum)])
            # print(f"After pick: ({i}, {currSum} ) : {dp[(i, currSum)]}")
            return dp[(i,currSum)]

        return True if dfs(0,0) else False