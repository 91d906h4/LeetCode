class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(string):
            piyo = {}
            fuga = ""
            temp = 0
            for j in string:
                if j not in piyo:
                    piyo[j] = temp
                    temp += 1
                fuga += str(piyo[j])
            return fuga
        
        pattern = helper(pattern)

        hoge = []
        for i, j in enumerate(words):
            if helper(j) == pattern: hoge.append(j)
        return hoge
