class Solution:
    def partitionString(self, s: str) -> int:
        res, temp = 1, ''

        for i in s:
            if i not in temp:
                temp += i
            else:
                temp = i
                res += 1
        
        return res
