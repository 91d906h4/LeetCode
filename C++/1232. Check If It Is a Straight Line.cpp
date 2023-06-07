class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int l = coordinates.size();

        if (l <= 2) return true;

        l--;

        int y1 = coordinates[0][1], x1 = coordinates[0][0],
            y2 = coordinates[l][1], x2 = coordinates[l][0];

        // check if a vertical line
        if (x2 - x1 == 0) {
            for (vector<int> &temp: coordinates) {
                if (temp[0] != x1) return false;
            }

            return true;
        }

        float a = ((y2 - y1) * 1.0) / (x2 - x1);
        float b = y1 - a * x1;

        for (vector<int> &temp: coordinates) {
            if (temp[1] != temp[0] * a + b) return false;
        }

        return true;
    }
};
