class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # for i in s:
        #     t = t.replace(i, "", 1)
        # return t

        for i, j in zip_longest(sorted(s), sorted(t)):
            if i != j:
                if i and i not in t: return i
                return j
