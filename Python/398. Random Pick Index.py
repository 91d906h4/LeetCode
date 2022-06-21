class Solution:

    def __init__(self, nums: List[int]):
        self.dict_ = defaultdict(list)
        for i, j in enumerate(nums):
            self.dict_[j].append(i)            

    def pick(self, target: int) -> int:
        return random.choice(self.dict_[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
