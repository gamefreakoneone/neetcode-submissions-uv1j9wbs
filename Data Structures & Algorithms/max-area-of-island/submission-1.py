class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        ROWS , COLS= len(grid) , len(grid[0])
        max_area = 0
        
        def traverse_area(origin_r , origin_c, area):
            for dr , dc in directions:
                r = origin_r + dr
                c = origin_c + dc
                if min(r , c) < 0 or r == ROWS or c==COLS or (r,c) in visited or grid[r][c]==0:
                    continue
                area += 1
                visited.add((r,c))
                area = traverse_area(r,c,area)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                area = 1
                visited.add((i,j))
                area = traverse_area(i,j, area)
                max_area = max(max_area, area)

        return max_area