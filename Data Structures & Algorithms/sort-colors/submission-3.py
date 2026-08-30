class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp 

        l = curr = 0
        r = len(nums) - 1
        
        while  curr <= r:
            if nums[curr] == 0: # All 0's to the left of the pointer
                swap(l , curr)
                l+=1
            elif nums[curr] == 2: # All 2's to the right of the pointer
                swap(curr , r)
                r -= 1
                curr-=1
            curr += 1