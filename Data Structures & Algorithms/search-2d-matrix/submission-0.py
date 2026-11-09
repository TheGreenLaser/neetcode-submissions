class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #two binary searches: one for row and one for column

        upper = 0
        lower = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while(lower >= upper):
            row = (upper + lower) // 2
            if matrix[row][right] < target:
                upper = row + 1
            elif matrix[row][left] > target:
                lower = row - 1
            else:
                upper = row
                lower = row
                break

        while(right >= left):
            col = (right + left) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = col + 1
            else:
                right = col - 1
        
        return False
