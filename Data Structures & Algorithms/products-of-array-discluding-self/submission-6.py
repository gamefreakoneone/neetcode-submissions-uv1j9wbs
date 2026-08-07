class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        product_arr = [1] * nums_len
        # LHP
        product = 1
        for i in range(1 , nums_len):
            product *= nums[i-1]
            product_arr[i] = product

        # RHP
        product = 1
        for i in range(nums_len-2, -1, -1):
            product *= nums[i+1]
            product_arr[i] *= product
        
        return product_arr
