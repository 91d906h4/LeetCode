class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        l = len(cost)

        cost.sort(reverse=True)

        for i in range(0, l, 3):
            res += cost[i]
            i += 1

            if i < l: res += cost[i]

        return res
