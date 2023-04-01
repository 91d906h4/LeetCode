class Solution {
public:
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        vector<int> res;

        for (int i = 0; i < s.length(); i++) {
            int temp = 0;
            int x = startPos[0], y = startPos[1];

            for (int j = i; j < s.length(); j++) {
                if (s[j] == 'R') y++;
                else if (s[j] == 'L') y--;
                else if (s[j] == 'D') x++;
                else if (s[j] == 'U') x--;
                
                if (0 <= x && x < n && 0 <= y && y < n) temp++;
                else break;
            }

            res.push_back(temp);
        }

        return res;
    }
};
