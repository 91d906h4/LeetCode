class Solution:
    def grayCode(self, n: int) -> List[int]:
#         hoge, fuga, piyo = ["0", "1"], [], []
#         for i in range(1, n):
#             fuga = ["0" + a for a in hoge]
#             piyo = ["1" + a for a in reversed(hoge)]
#             hoge = fuga+ piyo
#         return [int(a, 2) for a in hoge]
    
        return [(a ^ (a >> 1)) for a in range(2 ** n)]
