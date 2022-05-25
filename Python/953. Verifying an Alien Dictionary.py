class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict_ = {}
        for i, j in enumerate(order):
            dict_[j] = i
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False
                if words[i][j] != words[i + 1][j]:
                    if dict_[words[i][j]] > dict_[words[i + 1][j]]:return False
                    break
        return True
