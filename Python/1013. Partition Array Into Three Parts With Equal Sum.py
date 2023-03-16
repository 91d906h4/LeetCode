class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0: return False

        avg, temp, counter = sum(arr) // 3, 0, 0

        for i in arr:
            temp += i
            if temp == avg:
                temp = 0
                counter += 1

        return counter >= 3
