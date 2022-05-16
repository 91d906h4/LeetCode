class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        counter = [-1]
        t = 0
        for i in words:
            temp = 1
            for j in i:
                temp *= (ord(j) - ord('/'))
            if temp not in counter:
                counter.append(temp)
                result.append(i)
                counter.pop(0)
        return result
