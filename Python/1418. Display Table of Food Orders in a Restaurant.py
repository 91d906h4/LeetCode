class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        res, temp = {}, []

        for name, table, item in orders:
            if table not in res: res[table] = []
            if item not in temp: temp.append(item)
            res[table].append(item)
        
        temp.sort()
        res = sorted(res.items(), key = lambda x: int(x[0]))

        ans = [['Table'] + temp]
        for table, item in res:
            ans.append([table])
            for i in temp: ans[-1].append(str(item.count(i)))

        return ans
