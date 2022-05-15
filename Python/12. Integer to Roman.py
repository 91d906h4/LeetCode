class Solution:
    def intToRoman(self, num: int) -> str:
        dict_ = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        result = ""
        while num > 0:
            for i, j in reversed(dict_.items()):
                if num - i >= 0:
                    result = result + j
                    num -= i
                    break
        return result
