class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        i, j = 0, len(grid) - 1
        for m in grid:
            if m[i] == 0 or m[j] == 0: return False
            del m[i if i <= j else j]
            del m[j - 1 if i <= j else i - 1]
            if set(m) != set([0]): return False
            i += 1
            j -= 1
        return True
