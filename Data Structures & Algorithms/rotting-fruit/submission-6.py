from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0] , [-1, 0] , [0,-1] , [0,1]]
        fresh = 0
        time = 0
        ROWS , COLS = len(grid) , len(grid[0])
        rotten = deque()
        # visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh += 1
                    continue
                elif grid[i][j]==0:
                    continue
                rotten.append((i,j))
                # visited.add((i,j))

        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                i , j = rotten.popleft()
                for dr , dc in directions:
                    r , c = i + dr ,j + dc
                    if min(r,c) < 0 or r==ROWS or c==COLS or grid[r][c]!=1:
                        continue
                    # We are dealing with fresh fruit
                    grid[r][c] = 2
                    fresh -= 1
                    rotten.append((r,c))
            time += 1

        return time if fresh==0 else -1