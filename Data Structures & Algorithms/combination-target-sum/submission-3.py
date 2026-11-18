class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i , currSum):
            if currSum == target:
                result.append(subset.copy())
                return
            if i>=len(nums) or currSum > target:
                return
            
            currSum += nums[i]
            subset.append(nums[i])
            dfs(i , currSum)
            currSum -= nums[i]
            subset.pop()
            dfs(i+1 , currSum)
        
        dfs(0, 0)
        return result