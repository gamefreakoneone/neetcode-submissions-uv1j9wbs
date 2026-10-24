class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board) , len(board[0])
        visited = set()
        directions = [[1,0] , [-1,0], [0,1] , [0,-1]]
        
        def dfs( i , j, curr):
            if curr==len(word):
                return True
            for dr , dc in directions:
                r , c = i+dr , j+dc
                if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[curr] != board[r][c] or (r,c) in visited):
                    continue
                visited.add((r,c))
                if dfs(r,c , curr+1):
                    return True
                visited.remove((r,c))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    visited.add( (i , j) )
                    if dfs(i , j , 1):
                        return True
                    visited.remove((i,j))

        return False