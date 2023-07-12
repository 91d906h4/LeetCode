class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int a, b, i = k, j = k, n = nums.size(), res = nums[k], t = nums[k], m = 2;

        while (i > 0 || j < n - 1) {
            a = (i == 0) ? 0 : nums[i - 1];
            b = (j == n - 1) ? 0 : nums[j + 1];

            a < b ? j++ : i--;

            t = min(t, min(nums[i], nums[j]));
            res = max(res, t * m++);
        }

        return res;
    }
};
