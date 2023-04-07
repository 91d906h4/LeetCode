class Solution {
public:
    bool isHappy(int n) {
        int limit = 100, m = 0;

        while (n != 1 && limit > 0) {
            m = 0;
            
            while (n) {
                m += (n % 10) * (n % 10);
                n /= 10;
            }

            n = m;
            cout << m << endl;

            limit--;
        }

        return limit > 0;
    }
};
