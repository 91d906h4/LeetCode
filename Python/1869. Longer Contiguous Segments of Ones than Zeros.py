class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        temp = [""]
        for i in s:
            if set(i) == set(temp[-1]): temp[-1] += i
            else: temp.append(i)
        temp.pop(0)
        temp1 = []
        for i in temp:
            if i[0] == "1":
                temp1.append(i)
                temp.remove(i)
        temp.append("")
        temp1.append("")
        temp.sort(key = lambda x: len(x), reverse = True)
        temp1.sort(key = lambda x: len(x), reverse = True)
        return len(temp1[0]) > len(temp[0])
