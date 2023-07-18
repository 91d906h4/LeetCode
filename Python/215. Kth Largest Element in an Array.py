class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []

        # for i in nums:
        #     heapq.heappush(heap, i)

        #     if len(heap) > k: heapq.heappop(heap)

        # return heap[0]

        nums.sort(reverse=True)

        return nums[k - 1]
