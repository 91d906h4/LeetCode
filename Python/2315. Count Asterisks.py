class Solution:
    def countAsterisks(self, s: str) -> int:
        result, temp = 0, True
        for i in s:
            if i == "|": temp = not temp
            if temp and i =="*": result += 1
        return result
