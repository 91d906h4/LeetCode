class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        hoge = ""
        for i in words:
            hoge += i
            if hoge == s: return True
            if hoge not in s: return False
