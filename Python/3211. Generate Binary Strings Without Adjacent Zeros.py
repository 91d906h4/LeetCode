class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1: return ["0", "1"]

        result = ["0", "1"]
        n -= 1

        while n:
            temp0 = result
            temp1 = result
            temp = []

            for i in temp0:
                if i[-1] != "0":
                    temp.append(i + "0")

            for i in temp1:
                temp.append(i + "1")

            result = temp
            n -= 1

        return result
