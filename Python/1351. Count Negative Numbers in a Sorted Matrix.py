class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([x for x in sum(grid, []) if x < 0])
