class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m = str(blocks[:k]).count("W")
        r = m

        for i in range(k, len(blocks)):
            if blocks[i] == "W" and blocks[i - k] == "B": r += 1
            if blocks[i] == "B" and blocks[i - k] == "W": r -= 1

            m = min(m, r)

        return m
