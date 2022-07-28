class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for i, j in queries:
            dict_ = enumerate([x[(-1 * j):] for x in nums])
            dict_ = sorted(dict_, key = lambda x: x[1])
            result.append(dict_[i - 1][0])
        return result
