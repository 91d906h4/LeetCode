class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        l = len(cost)

        cost.sort(reverse=True)

        for i in range(0, l):
            if i % 3 == 2: continue

            res += cost[i]

        return res
