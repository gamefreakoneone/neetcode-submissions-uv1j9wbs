from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0, 1], [0, -1], [1,0] , [-1, 0]]
        ROW , COL = len(grid) , len(grid[0])


        def search_island( r, c):
            # if grid[r+dr][c+dc]== "0" or (r+dr , c+dc) in visited:
            #     return
            for dr, dc in directions:
                if min(r+dr , c+dc) < 0 or r+dr == ROW or c+dc == COL or grid[r+dr][c+dc]=="0" or (r+dr , c+dc) in visited:
                    continue
                visited.add((r+dr , c+dc))
                search_island(r+dr , c+dc)

        num_island = 0
        for i in range(ROW):
            for j in range(COL):
                if (i, j) in visited :
                    continue
                if grid[i][j]=="0":
                    visited.add((i, j))
                elif grid[i][j]=="1":
                    # Perform dfs to find rest of island
                    search_island(i , j)
                    num_island+=1

        return num_island