class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp, res = [], []

        for i, x in enumerate(s):
            if x == c: temp.append(i)
        
        for i, x in enumerate(s):
            m = 1001
            for j in temp: m = min(m, abs(i - j))
            res.append(m)
        
        return res
