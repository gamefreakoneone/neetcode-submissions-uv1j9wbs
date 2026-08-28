from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions= [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        ROWS , COLS = len(image) , len(image[0])
        queue = deque()
        queue.append((sr, sc))
        visited.add((sr,sc))
        compare = image[sr][sc]
        image[sr][sc]= color
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r , c = row+dr , col+dc
                if min(r,c )< 0 or r==ROWS or c==COLS or image[r][c] != compare or (r,c) in visited:
                    continue
                queue.append((r,c))
                image[r][c] = color
                visited.add((r,c))

        return image