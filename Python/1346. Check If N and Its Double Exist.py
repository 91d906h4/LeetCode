class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict_ = {}
        for i in arr:
            if i * 2 in dict_ or i / 2 in dict_: return True
            else: dict_[i] = 1
        return False
