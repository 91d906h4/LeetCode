class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int m = 0, temp = 0, r = grid.size(), c = grid[0].size();

        for(int i = 3; i <= r; i++){
            for(int j = 3; j <= c; j++){
                temp = grid[i - 3][j - 3] +
                       grid[i - 3][j - 2] +
                       grid[i - 3][j - 1] +
                       grid[i - 2][j - 2] +
                       grid[i - 1][j - 3] +
                       grid[i - 1][j - 2] +
                       grid[i - 1][j - 1];

                m = max(m, temp);
            }
        }

        return m;
    }
};
