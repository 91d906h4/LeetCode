class Solution {
public:
    vector<int> evenOddBit(int n) {
        int e = 0, o = 0;
        bool t = true;

        while (n > 0) {
            if (n % 2 == 1) {
                if (t) e++;
                else o++;
            }

            n /= 2;
            t = !t;
        }

        return {e, o};
    }
};
