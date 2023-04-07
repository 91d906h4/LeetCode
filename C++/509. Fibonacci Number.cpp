class Solution {
public:
    int fib(int n) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int f[n + 2];
        f[0] = 0; f[1] = 1;

        for (int i = 2; i <= n; i++) f[i] = f[i - 1] + f[i - 2];

        return f[n];
    }
};
