class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def gray():
            for i in range(2 ** n): yield i ^ (i >> 1)
        
        temp = list(gray())
        ptr = temp.index(start)

        return temp[ptr:] + temp[:ptr]
