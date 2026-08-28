from collections import deque

class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS , COLS = len(grid) , len(grid[0])
        visited = set()
        num_islands = 0
        def dfs(origin_r, origin_c):
            for dr , dc in directions:
                r = origin_r + dr
                c = origin_c +dc
                if min(r , c) < 0 or r == ROWS or c==COLS or (r,c) in visited or grid[r][c]=="0":
                    continue
                visited.add((r, c))
                dfs(r,c)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1" and (i , j) not in visited:
                    #Perform DFS here tos earch for all the pieces of the island
                    visited.add((i,j))
                    dfs(i , j)
                    num_islands += 1

        return num_islands