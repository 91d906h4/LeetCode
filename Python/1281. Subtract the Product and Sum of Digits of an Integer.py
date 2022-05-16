class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda result, value: result * int(value), list(str(n)), 1) - reduce(lambda result, value: result + int(value), list(str(n)), 0)
