import numpy
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        column = [max(x) for x in zip(*grid)]
        row = []
        for i in grid:
            row.append(max(i))
        width = len(column)
        length = len(row)
        result = 0
        for i in range(0, length):
            for j in range(0, width):
                result = result + min(row[i], column[j]) - grid[i][j]
        return result
