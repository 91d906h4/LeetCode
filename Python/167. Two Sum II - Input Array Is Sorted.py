class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
        while numbers[a] + numbers[b] != target:
            if numbers[b] + numbers[a] > target: b -= 1
            else: a += 1
        return [a + 1, b + 1]
