class Solution {
public:
    int reverse(int x) {
        string a, temp;
        bool k = false;
        long b = 1, n = x;

        if (x < 0) {
            b = -1;
            n *= -1;
        }

        a = to_string(n);

        for (int i = a.length() - 1; i >= 0; i--) {
            if (a[i] != 0) k = true;
            if (k) temp += a[i];
        }

        long res = stol(temp) * b;

        return (res < INT_MIN || res > INT_MAX) ? 0 : res;
    }
};
