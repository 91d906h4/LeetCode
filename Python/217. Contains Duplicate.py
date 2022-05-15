import collections

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         return collections.Counter(nums).most_common()[0][1] >= 2

        temp = set()
        for i in nums:
            if i in temp: return True
            temp.add(i)
        return False
