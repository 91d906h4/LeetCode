class Solution {
public:
    vector<int> leftRigthDifference(vector<int>& nums) {
        int total = 0;
        for(int i: nums) total += i;

        vector<int> res;
        int r = 0, l = total;

        for(int i: nums){
            r += i;
            res.push_back(abs(l - r));
            l -= i;
        }

        return res;
    }
};
