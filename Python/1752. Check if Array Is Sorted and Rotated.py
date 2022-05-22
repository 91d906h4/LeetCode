class Solution:
    def check(self, nums: List[int]) -> bool:
        return ",".join(map(str, sorted(nums))) in ",".join(map(str, nums + nums))
