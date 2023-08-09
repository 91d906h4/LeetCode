class Solution:
    def addMinimum(self, word: str) -> int:
        abc, pa, ps = "abc", 0, 0
        res = 0

        while ps < len(word):
            if abc[pa] == word[ps]: pa = (pa + 1) % 3; ps += 1
            else: res += 1; pa = (pa + 1) % 3

        return res + (3 - pa if pa != 0 else 0)
