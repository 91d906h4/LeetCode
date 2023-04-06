class Solution {
public:
    bool dfs(vector<vector<int>>& grid, int x, int y) {
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) return false;
        if (grid[x][y] == 1) return true;

        grid[x][y] = 1;

        bool a = dfs(grid, x + 1, y), b = dfs(grid, x - 1, y);
        bool c = dfs(grid, x, y + 1), d = dfs(grid, x, y - 1);

        return a && b&& c && d;
    }

    int closedIsland(vector<vector<int>>& grid) {
        int count = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0 && this->dfs(grid, i, j)) count++;
            }
        }

        return count;
    }
};
