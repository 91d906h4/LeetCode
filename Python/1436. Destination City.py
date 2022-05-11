class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = {}
        for i in paths:
            if i[1] not in city: city[i[1]] = 0
            city[i[0]] = 1
        return "".join([x for x , i in city.items() if i == 0])
