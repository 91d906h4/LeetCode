class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        temp, res, counter = {}, [], 0

        for a, b in zip(A, B):
            if a not in temp: temp[a] = 1
            else: temp[a] += 1; counter += 1

            if b not in temp: temp[b] = 1
            else: temp[b] += 1; counter += 1

            res.append(counter)

        return res
