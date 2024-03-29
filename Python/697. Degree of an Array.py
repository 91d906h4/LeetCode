class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hoge = sorted(Counter(nums).items(), key = lambda item: item[1], reverse = True)
        fuga = [x[0] for x in hoge if x[1] == hoge[0][1]]
        m = len(nums)
        n = m
        temp = nums[::-1]
        for i in fuga:
            m = min(m, n - temp.index(i) - nums.index(i))
            if m == 2: break
        return m
