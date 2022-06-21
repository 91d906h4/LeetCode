class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def helper(i):
            return any(x == "0" for x in str(i))
        
        i = n // 2 + 1
        while helper(i) or helper(n - i):
            i -= 1
        return [i, n - i]
