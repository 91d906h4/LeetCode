class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                return i
                break
