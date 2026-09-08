from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        visited=set()
        time = 0
        directions =[[1,0], [-1,0], [0,1] , [0,-1]]
        ROWS , COLS = len(grid) , len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten.append((i,j))

        while fresh >0 and rotten:
            for _ in range(len(rotten)):
                i , j = rotten.popleft()
                for dr , dc in directions:
                    r , c = i+dr , j+dc
                    if min(r,c) <0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c]==0:
                        continue
                    if grid[r][c]==1:
                        grid[r][c] = 0
                        rotten.append((r,c))
                        visited.add((r,c))
                        fresh-=1
            time += 1
        return time if fresh ==0 else -1