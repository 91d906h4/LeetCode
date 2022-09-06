class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        x, y = int(num1[0]), int(num2[0])
        m, n = int(num1[1].replace("i", "")), int(num2[1].replace("i", ""))
        return str(x * y - m * n) + "+" + str(x * n + y * m) + "i"
