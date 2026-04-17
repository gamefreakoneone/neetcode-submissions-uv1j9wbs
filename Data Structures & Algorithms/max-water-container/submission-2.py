class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0 , len(heights) - 1
        max_val= 0
        while l < r:
            min_height= min(heights[l] , heights[r])
            val = (r - l) * min_height
            if val > max_val:
                max_val = val
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_val
        