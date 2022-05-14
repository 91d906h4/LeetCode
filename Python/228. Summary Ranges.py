class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        index_a, index_b = 0, 0
        result = []
        for i in range(len(nums)):
            print(index_a, index_b)
            if i + 1 != len(nums) and nums[i + 1] == nums[i] + 1:
                index_b = i + 1
            else:
                if index_a != index_b: temp = str(nums[index_a]) + "->" + str(nums[index_b])
                else: temp = str(nums[index_b])
                result.append(temp)
                index_a = i + 1
                index_b = i + 1
        return result
