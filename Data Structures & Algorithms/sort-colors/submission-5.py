class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i , j):
            cache = nums[j]
            nums[j] = nums[i]
            nums[i] = cache
        
        l = 0
        r = len(nums) - 1
        curr = l
        while curr <= r:
            if nums[curr] == 0:
                swap(l, curr)
                l+= 1
            elif nums[curr]==2:
                swap(curr , r)
                r -= 1
                curr -= 1 # Because we need to check the new value
            curr+=1
        return nums
        