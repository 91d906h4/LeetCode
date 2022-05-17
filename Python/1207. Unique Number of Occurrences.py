class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = {}
        for i in arr:
            dict_[i] = dict_.get(i, 0) + 1
        temp = {}
        for _, i in dict_.items():
            if i not in temp: temp[i] = 0
            else: return False
        return True
