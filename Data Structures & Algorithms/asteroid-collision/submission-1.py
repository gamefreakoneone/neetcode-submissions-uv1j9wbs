class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while stack and stack[-1] > 0 and a < 0:
                pop_ast = stack.pop()
                if pop_ast > -a: # Right direction is more powerful
                    a = pop_ast
                    break
                elif pop_ast == -a:
                    alive = False
                    break
                
            if alive:
                stack.append(a)

        return stack