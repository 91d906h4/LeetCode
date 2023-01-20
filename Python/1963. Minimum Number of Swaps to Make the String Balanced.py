class Solution:
    def minSwaps(self, s: str) -> int:
        temp = []

        for i in s:
            if i == "]" and temp and temp[-1] == "[": temp.pop()
            else: temp.append(i)

        return math.ceil(Counter(temp)["["] / 2)
