class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

//         map<int, int> m;

//         for (int i: nums) {
//             if (m.count(i)) return true;
//             m[i] = 1;
//         }

//         return false;

        sort(nums.begin(), nums.end());

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i - 1] == nums[i]) return true;
        }

        return false;
    }
};
