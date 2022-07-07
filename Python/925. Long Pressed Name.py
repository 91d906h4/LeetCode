class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def _(s):
            s = list(s)
            temp = [s.pop(0)]
            for i in s:
                if i == temp[-1][0]: temp[-1] += i
                else: temp.append(i)
            return temp
        
        n, t = _(name), _(typed)
        if len(n) != len(t): return False
        for i, j in zip(n, t):
            if len(i) > len(j) or i[0] != j[0]: return False
        return True
