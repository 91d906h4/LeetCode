class Solution {
public:
    int partitionString(string s) {
        int temp[26] = {}, res = 1;

        for (char i: s) {
            int t = (int)i - 97;
            if (temp[t] == 0) temp[t] = 1;
            else {
                for (int i = 0; i < 26; i++) temp[i] = 0;
                temp[t] = 1;
                res++;
            }
        }

        return res;
    }
};
