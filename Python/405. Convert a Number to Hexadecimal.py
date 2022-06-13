class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        temp = "0123456789abcdef"
        result = ""
        for _ in range(8):
            result = temp[num & 15] + result
            num >>= 4
        return result.lstrip("0")
