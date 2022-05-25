class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        max_ = 0
        for i in range(len(satisfaction) + 1):
            temp = 0
            for j, k in enumerate(satisfaction[:i][::-1]):
                temp += (j + 1) * k
            if temp > max_: max_ = temp
        return max_
