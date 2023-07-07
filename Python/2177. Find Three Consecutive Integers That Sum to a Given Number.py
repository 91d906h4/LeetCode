class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num // 3
        b = num % 3

        if b == 0: return [a - 1, a, a + 1]
        return []
