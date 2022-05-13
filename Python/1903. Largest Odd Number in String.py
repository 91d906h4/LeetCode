class Solution:
    def largestOddNumber(self, num: str) -> str:
        temp = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                temp = i + 1
        return num[:temp]
