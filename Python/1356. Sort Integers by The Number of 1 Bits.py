class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        temp = {}
        for i in range(len(arr)):
            temp[i] = arr[i].bit_count()
        temp = sorted(temp.items(), key = lambda x: x[1])
        result = []
        for i in temp:
            result.append(arr[i[0]])
        return result
