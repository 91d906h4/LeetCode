class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in dominoes:
            i.sort()
        temp = {}
        for i in dominoes:
            if repr(i) not in temp: temp[repr(i)] = dominoes.count(i)
        result = 0
        for i in temp.values():
            result += (i - 1) * i // 2
        return result
