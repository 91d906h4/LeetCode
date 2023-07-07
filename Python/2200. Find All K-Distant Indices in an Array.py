class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        temp, res = [], set()

        for i, j in enumerate(nums):
            if j == key: temp.append(i)

        for i in temp:
            for j in range(max(0, i - k), min(i + k + 1, len(nums))):
                res.add(j)

        return sorted(list(res))
