class SORTracker:

    def __init__(self):
        self.temp = {}
        self.t_sorted = {}
        self.length = OrderedDict([])
        self.l_sorted = False
        self.count = 0

    def add(self, name: str, score: int) -> None:
        if score not in self.temp:
            self.temp[score] = [name]
            self.t_sorted[score] = True
            self.length[score] = 1
            self.l_sorted = False
        else:
            self.temp[score].append(name)
            self.t_sorted[score] = False
            self.length[score] += 1
            self.l_sorted = False

    def get(self) -> str:
        if not self.l_sorted:
            self.length = OrderedDict(sorted(self.length.items(), key=lambda x: x[0], reverse=True))
            self.l_sorted = True

        c = self.count

        for score, i in self.length.items():
            if c < i:
                if not self.t_sorted[score]:
                    self.temp[score].sort()
                    self.t_sorted[score] = True
                self.count += 1

                return self.temp[score][c]
            else: c -= i


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
