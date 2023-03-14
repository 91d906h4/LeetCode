class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0, temp = 0, res = nums.size() + 1;

        while (r < nums.size()) {
            temp += nums[r++];

            while (temp >= target) {
                res = min(res, r - l);
                temp -= nums[l++];
            }
        }

        if (res == nums.size() + 1) return 0;
        else return res;
    }
};
