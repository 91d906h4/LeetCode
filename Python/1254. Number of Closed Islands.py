class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        count = 0

        def dfs(x: int, y: int) -> bool:
            if x < 0 or x >= h or y < 0 or y >= w: return False
            if grid[x][y] == 1: return True

            grid[x][y] = 1

            a, b = dfs(x, y + 1), dfs(x, y - 1)
            c, d = dfs(x + 1, y), dfs(x - 1, y)

            return a and b and c and d
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and dfs(i, j): count += 1

        return count
