class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row, col = {}, {}
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(r):
            for j in range(c):
                if i in row or j in col:
                    matrix[i][j] = 0
