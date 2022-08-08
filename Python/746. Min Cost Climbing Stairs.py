class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
            print(cost)
        l = len(cost)
        return min(cost[l - 1], cost[l - 2])
