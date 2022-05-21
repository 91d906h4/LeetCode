class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result, i, j = 0, 1, 0
        while i < len(bank):
            if bank[i].count("1") == 0: i += 1
            else:
                result += bank[j].count("1") * bank[i].count("1")
                j = i
                i += 1
        return result
