import numpy as np

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)): grid[i].sort(reverse = True)
        for i in np.array(grid).T: res += max(i)

        return res
