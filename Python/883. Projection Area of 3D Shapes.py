import numpy as np

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return len([x for x in sum(grid, []) if x != 0]) + sum([max(x) for x in grid]) + sum([max(y) for y in np.array(grid).T])
