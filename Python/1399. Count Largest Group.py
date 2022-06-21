class Solution:
    def countLargestGroup(self, n: int) -> int:
        temp = Counter()
        for i in range(1, n + 1):
            hoge = sum((int(x) for x in str(i)))
            temp[hoge] += temp.get(hoge, 0) + 1
        return len([x[0] for x in temp.most_common() if x[1] == temp.most_common()[0][1]])
