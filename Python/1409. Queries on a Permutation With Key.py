class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [x for x in range(1, m + 1)]
        result = []
        for i in queries:
            temp = arr.index(i)
            arr.remove(i)
            arr.insert(0, i)
            result.append(temp)
        return result
