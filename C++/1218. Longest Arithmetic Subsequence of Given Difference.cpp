class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int m = 0, dp[40001] = {0};

        for (int i: arr) {
            i += 20001;
            dp[i] = dp[i - difference] != 0 ? dp[i - difference] + 1 : 1;
            m = max(m, dp[i]);
        }

        return m;
    }
};
