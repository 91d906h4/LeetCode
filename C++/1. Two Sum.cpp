class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        int temp;

        for(int i = 0; i < nums.size(); i++){
            temp = nums[i];

            if(m.count(temp)) return {m[temp], i};
            else m[target - temp] = i;
        }

        return {};
    }
};
