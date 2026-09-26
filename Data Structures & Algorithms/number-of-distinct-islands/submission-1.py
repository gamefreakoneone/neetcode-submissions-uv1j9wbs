class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions = [[1,0] , [-1, 0], [0,1], [0,-1]]
        uniqueIslands = set()
        islands_cache = []
        visited = set()
        ROWS , COLS = len(grid) , len(grid[0])
        
        def discover_island(i,j):
            for dr, dc in directions:
                r ,c = i+dr , j+dc
                if min(r,c) < 0 or r==ROWS or c==COLS or (r,c) in visited or grid[r][c]==0:
                    continue
                islands_cache.append((r,c))
                visited.add((r,c))
                discover_island(r,c)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                #Found an island
                visited.add((i,j))
                discover_island(i,j)
                zeroed_island = tuple(sorted((r-i , c-j) for r , c in islands_cache))
                uniqueIslands.add(zeroed_island)
                islands_cache =[]
        
        return len(uniqueIslands)