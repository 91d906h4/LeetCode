class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
#         return min(len([x for x in position if x % 2 == 0]), len(position) - len([x for x in position if x % 2 == 0]))

        l1, l2 = len(position), len([x for x in position if x % 2 == 0])
        return min(l1 - l2, l2)
