class Solution:
    def oddString(self, words: List[str]) -> str:
        def helper(string):
            temp = []
            for i in range(1, len(string)):
                temp.append(ord(string[i]) - ord(string[i - 1]))
            return ','.join(map(str, temp))
    
        temp = list(map(helper, words))
        hoge = Counter(temp)
        for i in hoge:
            if hoge[i] == 1: return words[temp.index(i)]
