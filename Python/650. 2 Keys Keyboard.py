class Solution:
    def minSteps(self, n: int) -> int:
        result, i = [], 2
        while n != 1:
            t = n % i
            if t == 0:
                result.append(i)
                n //= i
            else: i += 1
        return sum(result)
