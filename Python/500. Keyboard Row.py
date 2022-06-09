class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [x for x in words for n in [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")] if set(x.lower()).issubset(n)]
