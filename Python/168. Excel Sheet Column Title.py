class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            temp = columnNumber % 26
            if temp == 0: temp = 26
            result = chr(temp + 64) + result
            columnNumber = (columnNumber - temp) // 26
        return result
