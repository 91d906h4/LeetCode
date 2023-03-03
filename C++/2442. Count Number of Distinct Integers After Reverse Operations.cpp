class Solution {
public:
    int countDistinctIntegers(vector<int>& nums) {
        set<int> temp;
        string n;

        for(int i: nums){
            n = to_string(i);
            reverse(n.begin(), n.end());

            temp.insert(i);
            temp.insert(stoi(n));
        }

        return temp.size();
    }
};
