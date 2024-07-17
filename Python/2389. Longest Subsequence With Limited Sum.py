class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        result = []

        for q in queries:
            for i, n in enumerate(nums):
                if q < n:
                    result.append(i)
                    break
                else:
                    q -= n
            else:
                result.append(i + 1)

        return result
