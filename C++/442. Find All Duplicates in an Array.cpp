class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        map<int, int> m;
        vector<int> res;

        for(int i: nums) m[i]++;

        for(auto &[k, v]: m){
            if(v == 2) res.push_back(k);
        }

        return res;
    }
};
