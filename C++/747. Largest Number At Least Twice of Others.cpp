class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int res, temp = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > temp) {
                res = i;
                temp = nums[i];
            }
        }

        nums[res] = 0;

        for (int i: nums) {
            if (i * 2 > temp) return -1;
        }

        return res;
    }
};
