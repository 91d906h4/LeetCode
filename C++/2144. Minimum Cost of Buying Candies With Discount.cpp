class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.rbegin(), cost.rend());

        int res = 0, len = cost.size();

        for (int i = 0; i < len; i ++) {
            if (i % 3 == 2) continue;

            res += cost[i];
        }

        return res;
    }
};
