class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i , curr , total):
            if target == total:
                res.append(curr.copy())
                return

            for j in range(i , len(nums)):
                if total+nums[j] > target:
                    return # No point traversing rest of the list
                curr.append(nums[j])
                dfs(j,curr , nums[j]+total)
                curr.pop()

        
        dfs(0, [], 0)
        return res