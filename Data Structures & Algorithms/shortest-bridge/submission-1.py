from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        bridge = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        q = deque()
        n = len(grid)

        def discover_island(i,j):
            for dr, dc in directions:
                r , c = i + dr , j + dc
                if min(r,c) < 0 or r==n or c==n or (r,c) in visited or grid[r][c]==0:
                    continue
                visited.add((r,c))
                q.append((r,c))
                discover_island(r,c)

        # Search for iniital island
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    discover_island(i,j)
                    found = True
                    break # WE have found the first isalnd

        bridge = 0
        # Now perform BFS to find the shortest bridge
        while q:
            for _ in range(len(q)): # Searching the neighbors
                i , j = q.popleft()
                for dr , dc in directions:
                    r , c = i+dr , j+dc
                    if min(r,c) < 0 or r==n or c==n or (r,c) in visited:
                        continue
                    if grid[r][c] == 1:
                        return bridge
                    visited.add((r,c))
                    q.append((r,c))
            # Done searching the neighbors. None of them were island. Build a bridge
            bridge+=1
        return -1
