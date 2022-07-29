class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        temp = sorted(list(Counter(num).items()), reverse = True)
        k = []
        for i in temp:
            k.append(list(i))
        temp = k

        target = []
        for i, j in enumerate(num):
            if temp[0][1] == 0: temp.pop(0)
            if j == temp[0][0]:
                temp[0][1] -= 1
            else:
                target = [i, j]
                break
        target1 = [num.rfind(temp[0][0]), temp[0][0]]

        if len(target) == 0 or len(target1) == 0: return int(num)
        
        num = list(num)
        num[target[0]],  num[target1[0]] = target1[1], target[1]
        num = "".join(num)
        
        return int(num)
