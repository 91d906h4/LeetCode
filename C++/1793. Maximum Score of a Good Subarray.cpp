class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int i = k, j = k, n = nums.size(), res = nums[k], t = nums[k], m = 2;

        while (i > 0 || j < n - 1) {
            int a, b;

            if (i == 0) a = 0;
            else a = nums[i - 1];

            if (j == n - 1) b = 0;
            else b = nums[j + 1];

            if (a < b) j++;
            else i--;

            t = min(t, min(nums[i], nums[j]));
            res = max(res, t * m++);
        }

        return res;
    }
};
