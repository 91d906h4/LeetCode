class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict_ = {}
        for i in s:
            if i not in dict_: dict_[i] = 1
            else: return i
