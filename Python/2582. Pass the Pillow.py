class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= (n * 2 - 2)

        return time + 1 if time < n else n * 2 - time - 1
