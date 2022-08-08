class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#         l, p, r = len(p), Counter(p), []
#         t = Counter(s[:l])
#         if p == t: r.append(0)
#         for i in range(l, len(s)):
#             t[s[i]] += 1
#             t[s[i - l]] -= 1
#             if p == t: r.append(i - l + 1)
#         return r
        
        l, p, r = len(p), sum(hash(i) for i in p), []
        t = sum(hash(i) for i in s[:l])
        if p == t: r.append(0)
        for i in range(l, len(s)):
            t += hash(s[i]) - hash(s[i - l])
            if p == t: r.append(i - l + 1)
        return r
