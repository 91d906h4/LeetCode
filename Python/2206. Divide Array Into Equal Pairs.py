class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = []
        for i in nums:
            if i not in counter:
                counter.append(i)
            else:
                counter.remove(i)
        return len(counter) == 0
