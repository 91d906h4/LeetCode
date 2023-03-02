class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> temp;
        int m = 0;

        for(vector<int> i: points) temp.push_back(i[0]);

        sort(temp.begin(), temp.end());

        for(int i = 1; i < temp.size(); i++) m = max(m, temp[i] - temp[i - 1]);

        return m;
    }
};
