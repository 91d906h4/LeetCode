class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        result = 0
        while True:
            for i in target:
                if s.find(i) == -1: return result
                s = s.replace(i, "", 1)
            result += 1
