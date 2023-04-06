class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        ios::sync_with_stdio(false);
        cin.tie(NULL);

        sort(nums.begin(), nums.end());

        int i = 0, j = 0, l = nums.size();

        while (i < l && j < l) {
            if (nums[i] < nums[j]) i++;
            j++;
        }

        return i;
    }
};
