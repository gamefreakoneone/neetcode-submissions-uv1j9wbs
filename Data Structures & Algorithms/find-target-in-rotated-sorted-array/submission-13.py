class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        mid = (l+r)//2
        while l <= r:
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # The left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid  + 1
                else: # Target is on the left half
                    r = mid -1
            mid = (l+r)//2

        return -1