class Solution:
    def trap(self, height: List[int]) -> int:
        leftPass = [0] * len(height)
        rightPass = [0] * len(height)

        for i , n in enumerate(height):
            leftPass[i] = max(leftPass[i-1] , height[i])
        
        n = len(height)
        rightPass[n-1] = height[n-1] 

        for i in range(n - 2 , -1 , -1):
            rightPass[i] = max(rightPass[i+1] , height[i])

        volume = 0

        for i in range(n):
            volume += min(leftPass[i] , rightPass[i]) - height[i]
        
        return volume
