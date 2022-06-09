class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(x) for x in "".join(map(str, nums)).replace("0", " ").split()] + [0])
