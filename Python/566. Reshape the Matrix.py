class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c: return mat
        mat_t = []
        for i in mat:
            for j in i:
                mat_t.append(j)
        result = []
        x = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat_t[x])
                x += 1
            result.append(temp)
        return result
