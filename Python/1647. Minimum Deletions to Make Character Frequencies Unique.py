class Solution:
    def minDeletions(self, s: str) -> int:
        # dict_ = {}

        # for i in s:
        #     if i not in dict_: dict_[i] = 1
        #     else: dict_[i] += 1

        # temp = list(dict_.values())
        # temp.sort(reverse=True)

        # dict_ = {}
        # res = 0

        # for i in temp:
        #     if i not in dict_: dict_[i] = 1
        #     else:
        #         while i in dict_ and i > 0: i -= 1; res += 1
        #         dict_[i] = 1

        # return res

        temp = Counter(s)
        pointer = float("inf")
        res = 0

        for i in sorted(temp.values(), reverse=True):
            if i < pointer: pointer = i
            elif pointer == 0: res += i
            else:
                pointer -= 1
                res += i - pointer

        return res
