class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        temp = Counter(nums).values()
        r1, r2 = 0, 0
        for i in temp:
            if i & 1:
                r2 += 1
                i -= 1
            r1 += i // 2
        return [r1, r2]
