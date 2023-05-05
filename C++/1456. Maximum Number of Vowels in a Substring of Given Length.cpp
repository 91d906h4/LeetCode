class Solution {
public:
    inline bool isVowels(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int maxVowels(string s, int k) {
        queue<char> t;
        int m = 0, n = 0;

        for (char& i: s) {
            if (isVowels(i)) m++;
            t.push(i);

            if (!--k) break;
        }

        n = m;

        for (int i = k; i < s.length(); i++) {
            char a = t.front(), b = s[i];

            if (isVowels(a) && !isVowels(b)) n--;
            else if (!isVowels(a) && isVowels(b)) n++;

            m = max(m, n);

            t.push(s[i]);
            t.pop();
        }

        return m;
    }
};
