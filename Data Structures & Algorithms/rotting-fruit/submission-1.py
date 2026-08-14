from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows_size , cols_size = len(grid) , len(grid[0])
        visited = set()
        rotten = deque()

        for i in range(rows_size):
            for j in range(cols_size):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i , j))
                    visited.add((i,j))
        if fresh ==0:
            return 0
        directions = [ [1, 0] , [-1, 0], [0,1], [0,-1]]

        minutes = 0
        while rotten:
            for i in range(len(rotten)):
                r , c  = rotten.popleft()
                for rc , dc in directions:
                    row , col = r+rc , c+dc
                    if min(row , col) < 0 or row==rows_size or col == cols_size or grid[row][col]==0 or (row, col) in visited:
                        continue
                    visited.add((row, col))
                    rotten.append((row, col))
                    fresh -= 1
            minutes += 1
            if fresh == 0:
                return minutes
        
        return -1