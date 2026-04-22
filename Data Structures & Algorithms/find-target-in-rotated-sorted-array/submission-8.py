class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0,  len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]: # Indicating that left is sorted correctly
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]: #Indicating that it is right sorted
                if nums[r] >= target > nums[mid]:
                    l= mid+ 1
                else:
                    r = mid - 1
            else: # Binary Search
                if target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1

        return -1
        