class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        curr_largest = nums[0]
        tally= 1
        for i in range(1, len(nums)):
            if nums[i]==curr_largest:
                tally += 1
            else:
                tally -= 1
            if tally == 0:
                curr_largest = nums[i]
                tally += 1
        
        return curr_largest