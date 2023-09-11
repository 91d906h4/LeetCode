class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # dict_, result = {}, []
        # for i in range(len(groupSizes)):
        #     if groupSizes[i] not in dict_: dict_[groupSizes[i]] = [i]
        #     else: dict_[groupSizes[i]].append(i)
        # for i, j in dict_.items():
        #     result.append([])
        #     for k in range(len(j)):
        #         if len(result[-1]) < i: result[-1].append(j[k])
        #         else: result.append([j[k]])
        # return result

        temp, res = {}, []

        for i, x in enumerate(groupSizes):
            if x not in temp or temp[x] == []: temp[x] = [i]
            elif len(temp[x]) == x: res.append(temp[x]); temp[x] = [i]
            else: temp[x].append(i)

        res.extend(temp.values())

        return res
