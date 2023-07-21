class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []

        for i in range(100, 1000, 2):
            temp = Counter(digits)

            a = i // 100
            b = (i // 10) % 10
            c = i % 10

            if a not in temp: continue
            elif temp[a] == 0: continue
            else: temp[a] -= 1

            if b not in temp: continue
            elif temp[b] == 0: continue
            else: temp[b] -= 1

            if c not in temp: continue
            elif temp[c] == 0: continue

            res.append(i)

        return res
