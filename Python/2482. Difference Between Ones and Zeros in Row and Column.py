import numpy as np

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid_t = np.array(grid).T
        x, y = [], []
        m, n = len(grid), len(grid_t)

        for i in grid: x.append(i.count(1))
        for i in grid_t: y.append(list(i).count(1))

        return [[2 * i + 2 * j - m - n for j in y] for i in x]
