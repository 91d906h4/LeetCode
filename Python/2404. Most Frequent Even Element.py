class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        t = {}
        m, r = 1, 100001

        for i in nums:
            if i % 2: continue

            if i not in t: t[i] = 1
            else: t[i] += 1

            if t[i] == m and r > i: r = i
            elif t[i] > m:
                m, r = t[i], i

        return r if r != 100001 else -1
