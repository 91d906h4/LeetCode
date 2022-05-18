class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums).most_common()
        result = []
        for i in range(k):
            result.append(temp[i][0])
        return result
