class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        hoge = []
        fuga = [x for x in range(len(s) + 1)]
        print(fuga)
        for i in s:
            if i == "I": hoge.append(fuga.pop(0))
            else: hoge.append(fuga.pop())
        hoge.append(fuga[0])
        return hoge
