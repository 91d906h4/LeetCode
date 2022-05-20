class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        result = ""
        temp = ""
        if num < 0:
            temp = "-"
            num *= -1
        while num > 0:
            result = str(num % 7) + result
            num //= 7
        return temp + result
