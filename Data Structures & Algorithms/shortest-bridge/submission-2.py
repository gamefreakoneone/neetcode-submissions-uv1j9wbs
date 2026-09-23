from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[1,0] , [0, -1], [0,1], [-1, 0]]
        ROWS , COLS = len(grid) , len(grid[0])
        queue = deque()
        distance = 0
        visited = set()

        def dfs( i , j):
            for dr , dc in directions:
                r , c = i+dr , j+dc
                if min(r,c) < 0 or  r== ROWS  or c== COLS or grid[r][c]==0 or (r,c) in visited:
                    continue
                visited.add((r,c))
                queue.append((r,c))
                dfs(r, c)
                
        found = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    continue
                dfs(i,j) # We found the first island
                visited.add((i,j))
                queue.append((i,j))
                found= True
                break
            if found:
                break

        # Now we perform BFS

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dr , dc in directions:
                    r , c = i + dr , j + dc
                    if min(r, c) < 0 or r==ROWS or c==COLS or (r,c) in visited:
                        continue
                    if grid[r][c] == 1:
                        return distance
                    visited.add((r,c))
                    queue.append((r,c))
            distance += 1

        return -1


