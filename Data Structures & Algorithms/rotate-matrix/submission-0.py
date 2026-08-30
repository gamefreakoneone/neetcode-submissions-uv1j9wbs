class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l , r= 0, len(matrix) - 1 

        while l < r:
            for i in range(r-l):
                top , bottom  = l , r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom - i][l] #Top Left
                matrix[bottom-i][l] = matrix[bottom][r-i] # Bottom left
                matrix[bottom][r-i] = matrix[top+i][r] #Bottom Right
                matrix[top+i][r] = topLeft
            l+=1
            r-=1