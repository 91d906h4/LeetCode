class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        x = skill[0] + skill[-1]
        i, j = 0, len(skill) - 1
        res = 0

        while i < j:
            a, b = skill[i], skill[j]
            if (a + b != x): return -1

            res += a * b
            i, j = i + 1, j - 1

        return res
