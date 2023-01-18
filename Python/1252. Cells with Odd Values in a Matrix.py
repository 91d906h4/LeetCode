class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        x, y = [0] * m, [0] * n

        for i, j in indices:
            x[i] += 1
            y[j] += 1

        return len([1 for i in x for j in y if (i + j) % 2 == 1])
