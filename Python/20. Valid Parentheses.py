class Solution:
    def isValid(self, s: str) -> bool:
        hoge = []
        fuga = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in "([{": hoge.append(i)
            else:
                if len(hoge) and fuga[i] == hoge[-1]: hoge.pop()
                else: return False
        return len(hoge) == 0
