class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        brackets.insert(0, [0, 0])
        result = 0
        for i in range(1, len(brackets)):
            temp = brackets[i][0] - brackets[i - 1][0]
            r = brackets[i][1] / 100
            if income > temp:
                income -= temp
                result += temp * r
            else:
                result += income * r
                break
        return result
