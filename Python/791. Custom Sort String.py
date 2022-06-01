class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hoge = ""
        fuga = Counter(s)
        piyo = []
        for i in order:
            if i in fuga:
                hoge += i * fuga[i]
                fuga.pop(i)
                piyo.append(i)
        for i in piyo:
            s = s.replace(i, "")
        return hoge + s
