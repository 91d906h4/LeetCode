class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         temp = {}
#         for i in strs:
#             t = "".join(sorted(i))
#             if t not in temp: temp[t] = [i]
#             else: temp[t].append(i)
#         return [x[1] for x in temp.items()]

        temp = defaultdict(list)
        for i in strs:
            t = "".join(sorted(i))
            temp[t].append(i)
        return temp.values()
