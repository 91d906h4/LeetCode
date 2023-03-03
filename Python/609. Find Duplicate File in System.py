class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        temp, res = {}, []

        for i in paths:
            i = i.split()
            root, files = i[0], i[1:]

            for j in files:
                name, content = j[:j.rfind('(')], j[j.rfind('('):]
                name = root + "/" + name
                if content not in temp: temp[content] = [name]
                else: temp[content].append(name)

        return [x for x in temp.values() if len(x) > 1]
