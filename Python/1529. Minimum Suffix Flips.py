class Solution:
    def minFlips(self, target: str) -> int:
        res, temp = 0, '0'

        for i in target:
            if i != temp:
                res += 1
                temp = i
        
        return res
