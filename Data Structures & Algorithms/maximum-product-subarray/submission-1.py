class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = maxProd = nums[0]

        for num in nums[1:]:
            if num < 0:
                currMax , currMin = currMin , currMax
            
            currMax = max(num , currMax * num)
            currMin = min(num, currMin*num)
            maxProd = max(currMax, maxProd)

        return maxProd