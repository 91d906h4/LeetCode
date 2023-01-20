import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        t = np.rot90(np.array(matrix), 3)

        for i in range(l):
            for j in range(l):
                matrix[i][j] = t[i][j]
