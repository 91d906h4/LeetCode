class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        temp = 0
        for i in words:
            if i.startswith(pref): temp += 1
        return temp
