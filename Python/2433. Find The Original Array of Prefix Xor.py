class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        array = [pref[0]]
        for i in range(1, len(pref)):
            array.append(pref[i - 1] ^ pref[i])
        return array
