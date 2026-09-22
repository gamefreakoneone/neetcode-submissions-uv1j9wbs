from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0] , [0,-1], [0, 1]]
        queue = deque()
        ROWS , COLS= len(grid) , len(grid[0])
        visited = set()
        num_islands = 0

        def discover_island( i , j):
            for dr, dc in directions:
                r , c = i +dr , j + dc
                if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visited:
                    continue
                visited.add((r,c))
                discover_island(r, c)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="0" or (i, j) in visited : 
                    continue
                
                # THis means that the current coordinate is a piece of the isalns
                visited.add((i, j))
                discover_island( i , j)
                num_islands += 1

        return num_islands