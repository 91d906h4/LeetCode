class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c: return mat
        mat_t = []
        for i in mat:
            for j in i:
                mat_t.append(j)
        result = []
        x = 0

#         for i in range(r):
#             temp = []
#             for j in range(c):
#                 temp.append(mat_t[x])
#                 x += 1
#             result.append(temp)

        for i, element in enumerate(mat_t):
            if i % c == 0: result.append([])
            result[-1].append(element)

        return result
