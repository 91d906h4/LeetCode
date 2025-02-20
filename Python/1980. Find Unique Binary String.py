class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        table = {}

        for n in nums:
            table[int(n, 2)] = True

        for i in range(17):
            if i not in table:
                return "{0:b}".format(i).zfill(len(nums))
