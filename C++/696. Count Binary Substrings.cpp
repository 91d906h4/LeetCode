class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> temp;
        char t = s[0];
        int c = 0, res = 0;

        s += " ";

        for (char i: s) {
            if (i == t) c++;
            else {
                temp.push_back(c);
                t = i;
                c = 1;
            }
        }

        for (int i = 0; i < temp.size() - 1; i++) res += min(temp[i], temp[i + 1]);

        return res;
    }
};
