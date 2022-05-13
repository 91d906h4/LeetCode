class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict_ = {}
        for i in arr:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        temp = len(arr) * 0.25
        for i in dict_.items():
            print(i[0], i[1])
            if i[1] > temp:
                return i[0]
