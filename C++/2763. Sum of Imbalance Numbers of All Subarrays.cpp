class Solution {
public:
    int sumImbalanceNumbers(vector<int>& nums) {
        int n = nums.size(), res = 0;

        for (int i = 0; i < n; i++) {
            set<int> s;
            int t = 0;
            s.insert(nums[i]);

            for (int j = i + 1; j < n; j++) {
                if (s.count(nums[j]) != 0);
                else if (s.count(nums[j] + 1) == 0 && s.count(nums[j] - 1) == 0) t += 1;
                else if (s.count(nums[j] + 1) != 0 && s.count(nums[j] - 1) != 0) t -= 1;

                s.insert(nums[j]);
                res += t;
            }
        }

        return res;
    }
};
