class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int res = 0, i = 0, j = 0, l = nums.size();

        while (i < l && j < l) {
            if (nums[i] < nums[j]) {
                res++;
                i++;
            }
            j++;
        }

        return res;
    }
};
