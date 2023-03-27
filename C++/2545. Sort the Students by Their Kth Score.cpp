class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        vector<int> temp;
        map<int, int> dict;
        vector<vector<int>> res = score;

        for (int i = 0; i < score.size(); i++) {
            temp.push_back(score[i][k]);
            dict[score[i][k]] = i;
        }

        sort(temp.begin(), temp.end());

        for (int i = 0; i < temp.size(); i++) res[temp.size() - i - 1] = score[dict[temp[i]]];

        return res;
    }
};
