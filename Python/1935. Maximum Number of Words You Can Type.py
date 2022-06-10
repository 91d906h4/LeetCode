class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return len([x for x in text.split() if len(set(x).intersection(set(brokenLetters))) == 0])
