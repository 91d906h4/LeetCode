import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0

        heapq.heapify(nums)

        while True:
            m1 = heapq.heappop(nums)

            if not nums:
                break

            m2 = heapq.heappop(nums)

            if m1 >= k and m2 >= k:
                break

            heapq.heappush(nums, min(m1, m2) * 2 + max(m1, m2))

            result += 1

        return result
