class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, p, r = len(p), Counter(p), []
        t = Counter(s[:l])
        print(p, t)
        if p == t: r.append(0)
        for i in range(l, len(s)):
            t[s[i]] += 1
            t[s[i - l]] -= 1
            if p == t: r.append(i - l + 1)
        return r
