class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        temp = list(Counter(tasks).values())
        res = 0

        for i in temp:
            if i == 1: return -1
            elif i % 3 == 0: res += i // 3
            else: res += i // 3 + 1

        return res
