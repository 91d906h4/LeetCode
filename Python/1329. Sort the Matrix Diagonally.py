import numpy as np

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        temp = len(mat) - 1
        for i in range(temp, -1, -1):
            mat[i] = [0] * (temp - i) + mat[i] + [101] * i
        mat = np.array(mat)
        mat = mat.transpose()
        mat = list(map(sorted, mat))
        mat = np.array(mat)
        mat = mat.transpose()
        mat = list(map(list, mat))
        for i in range(temp + 1):
            mat[i] = mat[i][(temp - i):(len(mat[i]) if i == 0 else -i)]
        return mat
