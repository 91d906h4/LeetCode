class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        hoge, fuga = 0, 0
        for i, j in zip(s1, s2):
            if i >= j: hoge += 1
            if j >= i: fuga += 1
        return hoge == len(s1) or fuga == len(s2)
