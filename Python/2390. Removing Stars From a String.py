class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for i in s:
            if i == '*' and res != []: res.pop()
            else: res.append(i)
        
        return ''.join(res)
