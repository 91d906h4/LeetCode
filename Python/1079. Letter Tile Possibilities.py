class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        temp = Counter(tiles).values()
        temp = product(*map(lambda x: range(0, x + 1), temp))
        result = sum(factorial(sum(i)) // reduce(mul, map(factorial, i)) for i in temp) - 1
        return result
