class Solution:
    def smallestNumber(self, pattern: str) -> str:
        l = len(pattern)
        for i in permutations(range(1, l + 2)):
            for j, p in enumerate(pattern):
                if p == 'I' and not i[j] < i[j + 1]: break
                if p == 'D' and not i[j] > i[j + 1]: break
                if j == l - 1: return ''.join(map(str, i))
