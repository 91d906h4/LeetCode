class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string t = s + s;
        t[0] = ' '; t[t.length() - 1] = ' ';
        return t.find(s) == -1 ? false : true;
    }
};
