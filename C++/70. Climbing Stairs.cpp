class Solution {
public:
    int climbStairs(int n) {
        long long a = 1, b = 2, t;

        for (int i = 1; i < n; i++) {
            t = b;
            b += a;
            a = t;
        }

        return a;
    }
};
