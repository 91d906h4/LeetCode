class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        def dfs(x, y):
            if not (0 <= x < h) or not (0 <= y < w):
                return 0
            if grid[x][y] != 1:
                return 0
            grid[x][y] = -1
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
        
        max_ = 0
        for i in range(h):
            for j in range(w):
                temp = 0
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    max_ = max(max_, temp)
        
        return max_
