class Solution:
    def length(self, counter) -> int:
        return len([x for x, i in counter.items() if i > 0])

    def numSplits(self, s: str) -> int:
        l, r, res = Counter(), Counter(s), 0

        for i in s:
            if self.length(l) == self.length(r): res += 1
            l[i] += 1
            r[i] -= 1
        
        return res
