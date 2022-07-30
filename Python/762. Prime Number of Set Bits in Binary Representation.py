class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def helper(i):
            if i == 1: return False
            if i == 2: return True
            for j in range(2, i):
                if i % j == 0: return False
            return True
            
        result = 0
        for i in range(left, right + 1):
            result += 1 if helper(int(str(bin(i)).count("1"))) else 0
        return result
