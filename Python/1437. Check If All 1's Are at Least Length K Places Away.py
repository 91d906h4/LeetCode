class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        temp = k
        for i in nums:
            if i == 1:
                if temp < k: return False
                temp = 0
            else:
                temp += 1
        return True
