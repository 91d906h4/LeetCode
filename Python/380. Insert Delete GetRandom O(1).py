import random

class RandomizedSet:

    def __init__(self):
        self.dict_ = {}

    def insert(self, val: int) -> bool:
        if self.dict_.get(val, 0):
            return False
        else:
            self.dict_[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if self.dict_.get(val, 0):
            self.dict_.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.dict_.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
