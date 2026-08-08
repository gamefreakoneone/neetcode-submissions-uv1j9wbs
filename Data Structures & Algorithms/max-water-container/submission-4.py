class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_vol = 0
        while l < r:
            volume = min(heights[l] , heights[r]) * (r - l )
            max_vol = max(volume , max_vol)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1
        return max_vol
        