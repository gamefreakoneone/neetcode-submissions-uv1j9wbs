class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix) , len(matrix[0])
        i , j = 0 , 0
        while i < M:
            if (i + 1 < M and matrix[i][0] <= target < matrix[i+1][0]) or i == M-1: # This indicates that the number is in this row
                break # We are saving i
            i += 1

        # Now we iterate j

        while j < N:
            if matrix[i][j]==target:
                return True
            j += 1
        
        return False