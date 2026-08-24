class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if  i > 0 and nums[i]==nums[i-1] :
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    results.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                if target < 0:
                    l += 1
                if target > 0:
                    r -= 1
        
        return results
