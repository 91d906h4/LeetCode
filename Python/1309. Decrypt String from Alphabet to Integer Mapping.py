class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s[::-1]
        temp = []
        while s != "":
            if s[0] == "#":
                temp.append(s[:3][::-1])
                s = s[3:]
            else:
                temp.append(s[0][::-1])
                s = s[1:]
        temp = temp[::-1]
        result = ""
        for i in temp:
            if i in range(1, 10):
                result += chr(96 + i)
            else:
                result += chr(int(i[:2]) + 96)
        return result
