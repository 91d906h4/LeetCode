class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> m;
        int res = 0;

        for(int i: nums) m[i]++;

        for(auto &[_, i]: m){
            res += i * ((int)i - 1) / 2;
        }

        return res;
    }
};
