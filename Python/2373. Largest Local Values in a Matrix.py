class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l = len(grid) - 2
        r = []
        for i in range(l):
            t = []
            for j in range(l):
                t.append(max(sum([x[j:j + 3] for x in grid[i:i + 3]], [])))
            r.append(t)
        return r
