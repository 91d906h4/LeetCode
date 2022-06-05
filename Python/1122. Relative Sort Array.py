class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hoge = Counter(arr1)
        fuga = []
        for i in arr2:
            for _ in range(hoge[i]):
                fuga.append(i)
                arr1.remove(i)
        arr1.sort()
        for i in arr1:
            fuga.append(i)
        return fuga
