class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        temp = []
        result = []
        n = 0
        for i in list(str(num)):
            if int(i) % 2 == 0:
                even.append(i)
                temp.append(n)
            else:
                odd.append(i)
            n += 1
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        for i in range(0, (len(even) + len(odd))):
            if i in temp:
                result.append(even[0])
                even.pop(0)
            else:
                result.append(odd[0])
                odd.pop(0)
        return int("".join(result))
