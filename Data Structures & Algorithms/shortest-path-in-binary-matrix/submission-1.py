from collections import  deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        origin = (0,0)
        visited = set()
        visited.add((0,0))
        directions = [[1,0], [-1,0] , [0,1], [0,-1], [1,1], [-1,-1], [-1,1], [1,-1]]
        q = deque()
        q.append((0,0))
        ROW , COL = len(grid) , len(grid[0])
        path = 1
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                if row== ROW-1 and col==COL-1:
                        return path
                for dr, dc in directions:
                    r,c = row+dr , col+dc
                    if min(r,c) < 0 or r==ROW or c==COL or grid[r][c]==1 or (r,c) in visited:
                        continue
                    q.append((r,c))
                    visited.add((r,c))
            path += 1

        return -1