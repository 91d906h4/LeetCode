class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        temp = len(matrix)
        for i in range(temp):
            row = {x: 1 for x in range(1, temp + 1)}
            column = {x: 1 for x in range(1, temp + 1)}
            for j in range(temp):
                if matrix[i][j] in row:
                    row.pop(matrix[i][j])
                if matrix[j][i] in column:
                    column.pop(matrix[j][i])
            if len(row) != 0 or len(column) != 0: return False
        return True
