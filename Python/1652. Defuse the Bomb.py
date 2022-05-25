class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)
        temp = code * 2
        result = []
        n = 1
        if k < 0:
            n = len(code) + k
            k *= -1
        return [sum(temp[i + n:i + n + k]) for i in range(len(code))]
