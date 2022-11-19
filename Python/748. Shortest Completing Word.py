class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join([x for x in licensePlate if x not in ' 0123456789']).lower()
        licensePlate = Counter(licensePlate)
        
        def checker(c1, c2):
            for x in c2:
                if c1[x] < c2[x]: return False
            return True
        
        temp = '0' * 100000
        for i in words:
            if len(i) < len(temp) and checker(Counter(i), licensePlate): temp = i
        return temp
