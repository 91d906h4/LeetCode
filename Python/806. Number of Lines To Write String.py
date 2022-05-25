class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        hoge, fuga = 0, 1
        for i in s:
            piyo = widths[ord(i) - 97]
            if hoge + piyo <= 100:
                hoge += piyo
            else:
                hoge = piyo
                fuga += 1
        return [fuga, hoge]
