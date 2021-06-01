import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for x in range(0, math.floor(len(matrix)/2)):
            for y in range(0, math.ceil(len(matrix[x])/2)):
                temp = matrix[x][y]
                matrix[x][y] = matrix[len(matrix[x])-1-y][x]
                matrix[len(matrix[x])-1-y][x] = matrix[len(matrix[x])-1-x][len(matrix)-1-y]
                matrix[len(matrix[x])-1-x][len(matrix)-1-y] = matrix[y][len(matrix)-1-x]
                matrix[y][len(matrix)-1-x] = temp
                