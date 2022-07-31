class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = Counter()
        for i in range(len(messages)):
            d[senders[i]] += len(messages[i].split())
        d = d.most_common()
        d = sorted(d, key = lambda x: (x[1], x[0]), reverse = True)
        return d[0][0]
