class Solution {
public:
    bool isVowel(string target){
        char a = target[0], b = target[target.length() - 1];

        if ((a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') &&
            (b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u')) return true;
        else return false;
    }

    int vowelStrings(vector<string>& words, int left, int right) {
        int res = 0;

        for (int i = left; i <= right; i++) {
            if (isVowel(words[i])) res++;
        }

        return res;
    }
};
