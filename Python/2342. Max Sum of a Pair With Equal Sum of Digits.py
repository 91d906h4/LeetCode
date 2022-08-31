class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dict_ = defaultdict(list)
        for i in nums:
            dict_[sum(map(int, str(i)))].append(i)

        m = 0
        for i in dict_.values():
            i.sort()
            if len(i) >= 2: m = max(m, i[-1] + i[-2])
        return m if m != 0 else -1
