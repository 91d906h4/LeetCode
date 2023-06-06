class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # res1, res2 = [1], [1]
        # temp = 1

        # for i in range(1, len(nums)):
        #     temp *= nums[i - 1]

        #     res1.append(temp)

        # nums = nums[::-1]
        # temp = 1

        # for i in range(1, len(nums)):
        #     temp *= nums[i - 1]

        #     res2.append(temp)

        # print(res1, res2)

        # return [x * y for x, y in zip(res1, res2[::-1])]

        l = len(nums)
        res = [1] * l
        t1, t2 = 1, 1

        for i in range(1, l):
            t1 *= nums[i - 1]
            t2 *= nums[l - i]

            res[i] *= t1
            res[l - i - 1] *= t2

        return res
