class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = dict(Counter(magazine))
        r = dict(Counter(ransomNote))
        for i in r.items():
            if i[0] not in m or i[1] > m[i[0]]: return False
        return True
