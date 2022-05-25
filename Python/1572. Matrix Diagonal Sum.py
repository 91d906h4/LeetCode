class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)): result += mat[i][i] + mat[i] [::-1][i]
        if len(mat) % 2 == 1: result -= mat[len(mat) // 2][len(mat) // 2]
        return result
