class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        temp = 0
        number = list(number)
        for i in range(0, len(number)):
            print(number)
            if number[i] == digit:
                number.pop(i)
                temp = max(temp, int("".join(number)))
                number.insert(i, digit)
        return str(temp)
