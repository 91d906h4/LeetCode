class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict_ = {}
        for i, j in enumerate(nums):
            dict_[j] = i
        for [i, j] in operations:
            dict_[j] = dict_[i]
            del dict_[i]
        return dict(sorted(dict_.items(), key = lambda x: x[1])).keys()
