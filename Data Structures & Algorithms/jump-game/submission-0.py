class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        mem = {last: True}

        def dfs(i):
            if i in mem:
                return mem[i]
            
            for step in range(1, nums[i]+1):
                nxt = i + step
                if nxt <= last and dfs(nxt):
                    mem[nxt]= True
                    return True

            mem[i] = False
            return False
        
        return dfs(0)
