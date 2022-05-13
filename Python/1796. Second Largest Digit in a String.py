class Solution:
    def secondHighest(self, s: str) -> int:
        temp = []
        for i in list(s):
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] and i not in temp:
                temp.append(i)
        temp.sort(reverse=True)
        if len(temp) > 1: return temp[1]
        else: return -1
