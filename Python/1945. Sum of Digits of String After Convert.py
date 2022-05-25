class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        for i in s:
            temp += str(ord(i) - 96)
        for i in range(k):
            temp = sum(map(int, str(temp)))
        return temp
