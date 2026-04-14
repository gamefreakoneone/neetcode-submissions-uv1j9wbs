class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size_arr = len(nums)
        result = [1] * size_arr

        #LHP
        for i in range(1, size_arr):
            result[i] = result[i-1] * nums[i-1]
        
        #RHP
        right_product = 1
        for i in range(size_arr - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result