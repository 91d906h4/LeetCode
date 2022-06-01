class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
#         return [x[0] for x in Counter(nums).items() if x[1] == 1]

#         hoge = []
#         for i in nums:
#             if i not in hoge: hoge.append(i)
#             else: hoge.remove(i)
#         return hoge
        
        hoge = Counter()
        fuga = []
        for i in nums:
            hoge[i] += 1
        for i, j in hoge.items():
            if j == 1: fuga.append(i)
        return fuga
