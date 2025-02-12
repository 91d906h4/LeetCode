class Solution:
    @staticmethod
    def digsum(n: int) -> int:
        r = 0

        while n:
            r += n % 10
            n //= 10

        return r

    def maximumSum(self, nums: List[int]) -> int:
        # dict_ = defaultdict(list)
        # for i in nums:
        #     dict_[sum(map(int, str(i)))].append(i)

        # m = 0
        # for i in dict_.values():
        #     i.sort()
        #     if len(i) >= 2: m = max(m, i[-1] + i[-2])
        # return m if m != 0 else -1

        s2i = {}
        result = -1

        for i, n in enumerate(nums):
            s = self.digsum(n)

            if s not in s2i: s2i[s] = [i]
            else: s2i[s].append(i)

        for s, i in s2i.items():
            if len(i) <= 1: continue

            i = sorted(i, key=lambda i: nums[i], reverse=True)

            result = max(result, nums[i[0]] + nums[i[1]])

        return result
