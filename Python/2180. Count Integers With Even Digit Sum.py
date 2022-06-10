class Solution:
    def countEven(self, num: int) -> int:
        return (num - 1) // 2 if sum(int(n) for n in str(num)) % 2 else num // 2
