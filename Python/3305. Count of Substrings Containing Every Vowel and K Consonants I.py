class Solution:
    table = None

    def verify(self, k: int) -> bool:
        return self.table["a"] >= 1 and self.table["e"] >= 1 and self.table["i"] >= 1 \
           and self.table["o"] >= 1 and self.table["u"] >= 1 and self.table["_"] == k

    def update(self, c: str, w: int) -> None:
        if c in self.table: self.table[c] += w
        else: self.table["_"] += w

    def countOfSubstrings(self, word: str, k: int) -> int:
        r = 0

        for t in range(k + 5, len(word) + 1):
            # Init
            self.table = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "_": 0}

            for c in word[:t]:
                self.update(c, 1)

            if self.verify(k): r += 1

            for i in range(len(word) - t):
                self.update(word[i], -1)
                self.update(word[i+t], 1)

                if self.verify(k): r += 1

        return r
