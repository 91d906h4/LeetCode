class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int res = 0, t = nums[0], n = nums.size();

        if (n == 1) return t;

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) t += nums[i];
            else {
                res = max(res, t);
                t = nums[i];
            }
        }

        return max(res, t);
    }
};
