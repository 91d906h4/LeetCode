class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        res = max(special[0] - bottom, top - special[-1])

        for i in range(len(special) - 1):
            temp = special[i + 1] - special[i] - 1
            if temp > res: res = temp

        return res
