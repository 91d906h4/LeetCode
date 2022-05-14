class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        index_k, index_v = {}, {}
        value = s.split()
        key = list(pattern)
        if len(key) != len(value): return False
        for i, j in zip(key, value):
            if i not in index_k:
                index_k[i] = j
            else:
                if index_k[i] != j: return False
            if j not in index_v:
                index_v[j] = i
            else:
                if index_v[j] != i: return False
        return True
