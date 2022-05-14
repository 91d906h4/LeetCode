class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result, temp = 0, 1
        for i in reversed(columnTitle):
            result += (ord(i)- 64) * temp
            temp *= 26
        return result
