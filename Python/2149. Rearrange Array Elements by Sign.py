class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         nums = np.array(nums)
#         index_a = nums[nums > 0]
#         index_b = nums[nums < 0]
#         index = 0
#         result = []
#         for i in range(0, len(nums) // 2):
#             result.append(index_a[index])
#             result.append(index_b[index])
#             index += 1
#         return result

        size = len(nums)
        result = [0] * size
        index_a, index_b = 0, 1
        for i in nums:
            if i > 0:
                result[index_a] = i
                index_a += 2
            else:
                result[index_b] = i
                index_b += 2
        return result
