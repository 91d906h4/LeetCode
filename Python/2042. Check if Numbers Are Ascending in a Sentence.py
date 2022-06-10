class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        return all(int(i) < int(j) for i, j in zip(findall("\d+", s), findall("\d+", s)[1:]))
