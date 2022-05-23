class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = [[x, sum(mat[x])] for x in range(len(mat))]
        temp = sorted(temp, key = lambda x: (x[1], x[0]))
        return [x[0] for x in temp][:k]
