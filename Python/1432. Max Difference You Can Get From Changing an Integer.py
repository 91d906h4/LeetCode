class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)

        a, b = num, num

        for i, w in enumerate(num):
            if w != "9":
                a = num.replace(num[i], "9")
                break

        for i, w in enumerate(num):
            if w not in ["0", "1"]:
                b = num.replace(num[i], "1" if i == 0 else "0")
                break

        return int(a) - int(b)
