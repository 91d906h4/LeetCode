class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i+1] not in counter: counter[nums[i+1]] = 1
                else: counter[nums[i+1]] += 1
        return max(counter, key = counter.get)
