class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        result, t, r, u = "", "", False, ""
        if num < 0:
            t = "-"
            num *= -1
            temp = Counter(str(num))
            r = True
        else:
            temp = Counter(str(num))
            min_ = 10
            for i in temp.keys():
                i = int(i)
                if i < min_ and i != 0: min_ = i
            temp[str(min_)] -= 1
            u = str(min_)
        temp = sorted(temp.items(), key = lambda x: int(x[0]), reverse = r)
        for i, j in temp:
            result += str(i) * j
        return t + u + result
