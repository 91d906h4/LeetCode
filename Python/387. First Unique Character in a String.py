class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_ = {}
        for i in s:
            if i not in dict_: dict_[i] = 1
            else: dict_[i] += 1
        dict_ = sorted(dict_.items(), key = lambda x: x[1] and x[1] == 1, reverse = True)
        if dict_[0][1] == 1: return s.index(dict_[0][0])
        else: return -1
