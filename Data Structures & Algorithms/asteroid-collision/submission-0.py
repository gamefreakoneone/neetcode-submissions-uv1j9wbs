class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0: # Collision
                if abs(stack[-1]) > abs(asteroid):
                    asteroid = 0
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    asteroid = 0
            if not asteroid:
                continue
            else:
                stack.append(asteroid)
        
        return stack
            
