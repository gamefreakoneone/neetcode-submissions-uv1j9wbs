class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0] , [1,0] , [0,1] , [0, -1]]
        visited = set()
        num_islands = 0
        ROWS , COLS = len(grid) , len(grid[0])
        def dfs(i , j):
            for dr , dc in directions:
                r ,c = i+dr , j+dc
                if min(r,c) < 0 or r==ROWS or c==COLS or grid[r][c]=="0" or (r,c) in visited:
                    continue
                visited.add((r,c))
                dfs(r,c)
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in visited or grid[i][j]=="0":
                    continue
                visited.add((i,j))
                dfs(i,j)
                num_islands+=1
        return num_islands