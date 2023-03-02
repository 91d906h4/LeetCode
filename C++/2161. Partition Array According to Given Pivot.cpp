class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> l, r, x;

        for(int i: nums){
            if(i < pivot) l.push_back(i);
            else if(i == pivot) x.push_back(i);
            else r.push_back(i);
        }

        for(int i: x) l.push_back(i);
        for(int i: r) l.push_back(i);

        return l;
    }
};
