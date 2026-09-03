class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        # Initialize the row and col
        row, col = 0, m - 1

        # Traverse the matrix from (0, m-1):
        while row < n and col >= 0:
            
            # Return true if target is found
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False 
        