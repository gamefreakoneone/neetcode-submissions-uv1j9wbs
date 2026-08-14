class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        storedIslands = set()
        visitedLand = set()
        row_size , col_size = len(grid) , len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        stored_directions_CACHE = []
        def search_island( i , j):
            for dr, dc in directions:
                row , col = i + dr , j+dc 
                if min(row, col) < 0 or row == row_size or col == col_size or (row , col) in visitedLand or not grid[row][col]:
                    continue
                visitedLand.add((row, col))
                stored_directions_CACHE.append([row , col])
                search_island(row, col)

        # def normalization(origin_r, origin_c):
        #     for i in range(len(stored_directions_CACHE)):
        #         row, col = stored_directions_CACHE[i]
        #         normalized_row = row - origin_r
        #         normalized_col = col - origin_c
        #         stored_directions_CACHE[i] = [normalized_row , normalized_col]
                
        
        for i in range(row_size):
            for j in range(col_size):
                # The idea is that we find the first land and if land present, use dfs to find the island. Using the origin 
                if not grid[i][j] or (i,j) in visitedLand:
                    continue
                if grid[i][j] == 1: # Find the first isalnd
                    origin_r , origin_c = i , j
                    visitedLand.add((origin_r , origin_c))
                    stored_directions_CACHE.append([origin_r , origin_c])
                    search_island(origin_r, origin_c)
                    # normalization(origin_r, origin_c)
                    storedIslands.add(tuple(sorted((r - i , c - j ) for r , c in stored_directions_CACHE)))
                    # Reinitalize stored_directions_CACHE
                    stored_directions_CACHE= []
        
        return len(storedIslands)