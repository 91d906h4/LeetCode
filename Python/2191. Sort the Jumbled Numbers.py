class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x: int("".join([str(mapping[int(y)]) for y in str(x)])))
