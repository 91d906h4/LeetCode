class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);

        int l = cost.size();

        for (int i = 2; i < cost.size(); i++) cost[i] += min(cost[i - 1], cost[i - 2]);

        return min(cost[l - 1], cost[l - 2]);
    }
};
