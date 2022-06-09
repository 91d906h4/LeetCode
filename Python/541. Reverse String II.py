class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), k * 2):
            s = s[:i] + "".join(reversed(s[i:i + k])) + s[i + k:]
        return s
