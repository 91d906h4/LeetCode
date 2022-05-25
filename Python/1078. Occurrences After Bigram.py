class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        hoge = text.split()
        fuga = []
        for i in range(len(hoge) - 2):
            if hoge[i] == first and hoge[i + 1] == second: fuga.append(hoge[i + 2])
        return fuga
