class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0, 0)
        dict_ = {}
        for i in range(len(releaseTimes) - 1):
            temp = releaseTimes[i + 1 ] - releaseTimes[i]
            if keysPressed[i] not in dict_:
                dict_[keysPressed[i]] = temp
            else:
                dict_[keysPressed[i]] = max(dict_[keysPressed[i]], temp)
        dict_ = sorted(dict_.items(), key = lambda x: (x[1], x[0]), reverse = True)
        print(dict_)
        return dict_[0][0]
