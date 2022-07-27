class ATM:

    def __init__(self):
        self.list_ = [20, 50, 100, 200, 500]
        self.temp = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, j in enumerate(banknotesCount):
            self.temp[i] += j

    def withdraw(self, amount: int) -> List[int]:
        i = 4
        t = copy.deepcopy(self.temp)
        out = [0, 0, 0, 0, 0]
        while(amount > 0 and i != -1):
            a = amount // self.list_[i]
            if a >= 1 and self.temp[i] > 0:
                a = min(a, self.temp[i])
                amount -= a * self.list_[i]
                out[i] += a
                self.temp[i] -= a
            else: i -= 1
        if amount == 0: return out
        else:
            self.temp = t
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
