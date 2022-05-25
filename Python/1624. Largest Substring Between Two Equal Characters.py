class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         if len(set(s)) == len(s): return -1
#         max_ = 0
#         hoge = [x[0] for x in Counter(s).items() if x[1] > 1]
#         for i in hoge:
#             max_ = max(max_, s.rfind(i) - s.find(i) - 1)
#         return max_
        
        max_ = -1
        for i in s:
            max_ = max(max_, s.rfind(i) - s.find(i) - 1)
        return max_
