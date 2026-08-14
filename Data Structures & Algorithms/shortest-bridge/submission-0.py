from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows_size , col_size = len(grid) , len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        queue = deque()

        def dfs(i , j):
            for dr , dc in directions:
                row , col = dr+ i, dc+ j
                if  (row, col) in visited or row == rows_size or col == col_size or min(row , col) < 0 or not grid[row][col] :
                    continue
                visited.add((row, col))
                queue.append((row, col)) # So we dont have to break the inital loop for loop and then perform BFS ina  different loop?
                dfs(row, col)
        
        def bfs():
            levels = 0
            while queue:
                for i in range(len(queue)):
                    r , c = queue.popleft()
                    for dr, dc in directions:
                        row , col = dr+ r, dc+ c
                        if  row == rows_size or col == col_size or min(row , col) < 0 or (row, col) in visited :
                            continue
                        if grid[row][col] == 1:
                            return levels
                        queue.append((row, col))
                        visited.add((row, col))

                levels += 1
            return 0
        result = 0
        for i in range(rows_size):
            for j in range(col_size):
                if not grid[i][j] or (i , j) in visited:
                    continue
                # Encountered Land. FInd the rest of the island and break
                visited.add((i, j))
                queue.append((i, j))
                dfs(i , j)
                result = bfs()
                break
            if result:
                break
        
        return result
