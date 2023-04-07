class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int l = nums.size();

        bool increase = nums[0] < nums[l - 1];

        for (int i = 1; i < nums.size(); i++) {
            if (increase && nums[i - 1] > nums[i]) return false;
            else if (!increase && nums[i - 1] < nums[i]) return false; 
        }

        return true;
    }
};
