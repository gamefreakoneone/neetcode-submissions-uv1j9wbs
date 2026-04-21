class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        mid = int((l+r)/2)
        lowest = nums[0]
        while l < r:
            if  nums[mid] < lowest:
                lowest = nums[mid]
            if nums[mid] > nums[r]: # Array is still rotated
                l = mid + 1
            elif nums[mid] < nums[r]:
                r =  mid 
            mid = int((l+r)/2)
        lowest = min(lowest, nums[mid])
        return lowest