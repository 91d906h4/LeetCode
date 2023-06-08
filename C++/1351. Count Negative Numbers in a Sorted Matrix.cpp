class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int res = 0, length = grid[0].size(), l, r, m;

        for (vector<int> temp: grid) {
            if (temp[0] < 0) {
                res += length;
                continue;
            }

            l = 0, r = length - 1;

            while (l <= r) {
                m = (l + r) / 2;
                if (temp[m] < 0) r = m - 1;
                else l = m + 1;
            }

            res += length - l;
        }

        return res;
    }
};
