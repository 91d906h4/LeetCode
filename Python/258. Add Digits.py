class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        temp = num % 9
        if temp == 0: return 9
        else: return temp
