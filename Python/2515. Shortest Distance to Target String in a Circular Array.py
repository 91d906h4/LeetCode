class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res, l = [], len(words)

        for i in range(l):
            if words[i] == target: res.append(i)

        m = 101
        for i in res:
            m = min(m, abs(i - startIndex), abs(l - i + startIndex), abs(l + i - startIndex))
        
        return m if m != 101 else -1
