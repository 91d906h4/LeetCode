class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in ops:
            if i == "C":
                result.pop()
            elif i == "D":
                result.append(result[-1] * 2)
            elif i == "+":
                result.append(result[-2] + result[-1])
            else:
                result.append(int(i))
        return sum(result)
