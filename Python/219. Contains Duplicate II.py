class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] not in dict_: dict_[nums[i]] = [i]
            else: dict_[nums[i]].append(i)
        for i in dict_.values():
            i.sort()
            for j in range(len(i) - 1):
                if abs(i[j] - i[j + 1]) <= k: return True
        return False
